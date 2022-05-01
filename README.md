# BACKEND-CHALLENGE-MEDICAR

# Sumário

- [Sobre o desafio](#sobre)
- [Requisitos técnicos](#requisitos)
- [Tecnologias utilizadas](#requisitos)
- [Comandos para instalar na sua maquina](#instalação)
- [Execução do projeto](#execução)

# Sobre

 Implementar uma interface administrativa na qual o gestor da clínica (superusuário) poderá cadastrar um médico e criar a agenda do médico.

# Requisitos

- Cadastrar médicos
- Criar agenda para médico

# Técnologias 

  - [Python3](https://www.python.org/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [sqlite3](https://docs.python.org/3/library/sqlite3.html)
 
# Instalação

1. Clone o repositório

2. Crie o ambiente virtual para o projeto:

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências:

- `python3 -m pip install -r dev-requirements.txt`


# Execução

Crie um super usuário:

Passo 1: Criar o super usuário

  - `python manage.py createsuperuser`


Passo 2: Digite no terminal o comando para subir o servidor:

  - `python manage.py runserver`
  

Passo 3: Entre no endereço http://localhost:8000/admin/ para fazer o login com o usuário criado.


Passo 4: Crie um médico e crie a agenda do médico.


Passo 5: Entre no endereço http://localhost:8000 para ver os endpoints criados.

