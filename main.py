# Descrição: Crie um sistema para gerenciar tarefas de usuários, incluindo categorias, prazos e status de conclusão. O sistema deve permitir cadastrar, atualizar, excluir e listar tarefas de forma organizada.

#                                 C  R   U   D 

from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import argparse

db = create_engine("sqlite:///testedban.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Gerenciador(Base):

    __tablename__="gerenciador"

    id    = Column("id", Integer, primary_key=True, autoincrement=True)
    nome  = Column("nome", String)
    email = Column("email", String)

    def __init__(self, nome, email):
        self.nome = nome 
        self.email = email

class Tarefas(Base):

    __tablename__="tarefas"
    id        = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo    = Column("titulo", String)
    descrição = Column("descrição", String)
    prazo     = Column("prazo", Date)
    status    = Column("status", String)
    categoria = Column("categoria", String)
    usuario   = Column("usuario", ForeignKey("gerenciador.id"))

    def __init__(self, titulo, descrição, prazo,usuario,categoria,status,):
        self.titulo    = titulo
        self.descrição = descrição
        self.prazo     = prazo
        self.categoria = categoria
        self.usuario   = usuario
        self.status    = status

class Categorias(Base):

    __tablename__="categorias"
    id       = Column("id", Integer, primary_key=True, autoincrement=True)
    trabalho = Column("trabalho", String)
    pessoal  = Column("pessoal", String)
    estudos  = Column("estudos", String)

    def __init__(self,trabalho,pessoal,estudos):
        self.trabalho = trabalho
        self.pessoal  = pessoal
        self.estudos  = estudos

Base.metadata.create_all(bind=db)

#  EXEMPLOS DE TESTE 

# usuario = Gerenciador(nome="ablo", email="emailexe@gmail.com")

# session.add(usuario)
# session.commit()  

# # session.delete(usuario)
# # session.commit()

# tarefas = Tarefas(
#     titulo="Fazer commit no projeto",
#     descrição="Projeto de sistemas de organização",
#     prazo="21/12",
#     categoria="taf teste",
#     status="pendente",
#     usuario=usuario.id
#     )

# session.add(tarefas)
# session.commit()


# # FILTRO 
# # usuario_fil = session.query(Tarefas).filter_by(usuario=usuario.id,categoria="taf teste",status= "pendente")



# session.delete(tarefas)
# session.commit()

# CLI Command-Line Interface | Interface de Linha de Comando

def add_task(titulo,descrição,prazo,usuario,categoria,status): 
    from datetime import datetime
    try:
        prazo_data = datetime.strptime(prazo, "%Y-%m-%d").date()
        nova_descrição = Tarefas(
            titulo    = titulo, 
            descrição = descrição, 
            prazo     = prazo_data,
            usuario   = usuario,
            categoria = categoria,
            status    = status
            )
        session.add(nova_descrição)
        session.commit()
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar tarefas: {e}")


def list_task():
    tarefas = session.query(Tarefas).all()
    if tarefas:
        for tarefa in tarefas: 
            print(f"[{tarefa.id}] {tarefas.titulo} - {tarefas.descrição} (Prazo: {tarefas.prazo})")
    else:
        print("Nenhum tarefas encontrada.")

# Configuração de CLI 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerenciador de Tarefas")
    subparsers = parser.add_subparsers(dest="command")

    # Comando para adicionar tarefas
    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("titulo")
    add_task_parser.add_argument("descrição")
    add_task_parser.add_argument("prazo")  # Formato YYYY-MM-DD
    add_task_parser.add_argument("usuario")
    add_task_parser.add_argument("categoria")
    add_task_parser.add_argument("status")

    # Comandos para listar tarefas
    list_task_parser = subparsers.add_parser("list-tasks")

    args = parser.parse_args()

    if args.command == "add-task":
        add_task(args.titulo, args.descrição, args.prazo, args.usuario, args.categoria, args.status)
    elif args.command == "list-tasks":
        list_task()
    else:
        print("Comando não reconhecido.")
    