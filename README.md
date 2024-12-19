# CRUD Básico com SQLAlchemy

Este é um projeto simples que implementa as operações básicas de um CRUD (Create, Read, Update, Delete) usando SQLAlchemy e SQLite. O sistema gerencia tarefas, permitindo adicioná-las, listá-las, atualizá-las e excluí-las.

## Requisitos

- Python 3.7 ou superior
- Biblioteca `SQLAlchemy`

Para instalar o SQLAlchemy:
```bash
pip install sqlalchemy
```

## Estrutura do Banco de Dados

A aplicação utiliza um modelo simples para gerenciar tarefas. Cada tarefa possui os seguintes campos:

- **id**: Identificador único da tarefa (gerado automaticamente).
- **titulo**: Título da tarefa.
- **descrição**: Descrição da tarefa.
- **prazo**: Prazo da tarefa (formato `YYYY-MM-DD`).
- **usuario**: Nome do usuário associado à tarefa.
- **categoria**: Categoria da tarefa.
- **status**: Status da tarefa (exemplo: "Pendente", "Concluída").

## Operações Disponíveis

### 1. Criar uma Nova Tarefa
Adiciona uma nova tarefa ao banco de dados.
```python
from datetime import datetime

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
```

### 2. Listar Tarefas
Exibe todas as tarefas registradas no banco de dados.
```python
def list_task():
    tarefas = session.query(Tarefas).all()
    if tarefas:
        for tarefa in tarefas: 
            print(f"[{tarefa.id}] {tarefas.titulo} - {tarefas.descrição} (Prazo: {tarefas.prazo})")
    else:
        print("Nenhum tarefas encontrada.")
```

### 3. Atualizar uma Tarefa
Atualiza os dados de uma tarefa existente.
```python
def update_task(tarefa_id, titulo=None, descrição=None, prazo=None, status=None):
    tarefa = session.query(Tarefa).get(tarefa_id)
    if tarefa:
        if titulo:
            tarefa.titulo = titulo
        if descrição:
            tarefa.descrição = descrição
        if prazo:
            tarefa.prazo = datetime.strptime(prazo, "%Y-%m-%d").date()
        if status:
            tarefa.status = status
        session.commit()
```

### 4. Excluir uma Tarefa
Remove uma tarefa do banco de dados.
```python
def delete_task(tarefa_id):
    tarefa = session.query(Tarefa).get(tarefa_id)
    if task:
        session.delete(tarefa)
        session.commit()
```

## Executando o Projeto

1. Certifique-se de que o banco de dados foi configurado:
```python
Base.metadata.create_all(bind=db)
```

2. Utilize as funções para interagir com o banco de dados.

**Exemplo de Adição de uma Tarefa:**
```python
add_task(
    titulo="Estudar SQLAlchemy",
    descrição="Aprender o básico de ORM com Python",
    prazo="2024-12-20",
    usuario="João",
    categoria="Estudo",
    status="Pendente"
)
```

3. Liste as tarefas:
```python
list_tasks()
```

## Licença
Este projeto é livre para uso e modificação.

