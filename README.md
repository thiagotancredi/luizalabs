
---

# Projeto API de Favoritos

Este projeto é uma API construída com **FastAPI** para gerenciar o fluxo de favoritar produtos. A API permite:

- CRUD de usuários.
- Listagem de produtos.
- Listagem de produtos favoritos.
- Criação e remoção de produtos favoritos para usuários autenticados.

A aplicação utiliza **SQLAlchemy** para interação com o banco de dados, **JWT** para autenticação e autorização, e **Docker** para simplificar a execução do ambiente.

## Dependências Principais

- **Python**: ^3.12
- **FastAPI**: ^0.115.0
- **SQLAlchemy**: ^2.0.35
- **Pydantic Settings**: ^2.5.2
- **Pwdlib**: ^0.2.1 (com Argon2)
- **PyJWT**: ^2.9.0
- **FastAPI Pagination**: ^0.12.27
- **Psycopg**: ^3.2.2

### Dependências de Desenvolvimento

- **pytest-cov**: ^5.0.0
- **taskipy**: ^1.13.0
- **ruff**: ^0.6.5
- **httpx**: ^0.27.2
- **pytest**: ^8.3.3
- **testcontainers**: ^4.8.1
- **factory-boy**: ^3.3.1
- **faker**: ^29.0.0
- **freezegun**: ^1.5.1

## Requisitos

- **Docker**
- **Poetry**

Você deve ter o Docker e o Poetry instalados para rodar o projeto.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/thiagotancredi/luizalabs.git
   cd luizalabs
   ```

2. Crie o arquivo `.env` com as variáveis de ambiente. Use os comandos abaixo conforme seu sistema operacional:

   - **Para Linux ou macOS:**
     ```bash
     echo -e "DATABASE_URL=\"postgresql+psycopg://app_user:app_password@localhost:5432/app_db\"\nSECRET_KEY=\"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\"\nALGORITHM=\"HS256\"\nACCESS_TOKEN_EXPIRE_MINUTES=30" > .env
     ```

   - **Para Windows (cmd):**
     ```bash
     echo DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db" > .env
     echo SECRET_KEY="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" >> .env
     echo ALGORITHM="HS256" >> .env
     echo ACCESS_TOKEN_EXPIRE_MINUTES=30 >> .env
     ```

### Verificando o arquivo `.env`

Depois de criar o arquivo `.env`, verifique se ele foi criado corretamente com:

- **Linux/macOS:**
  ```bash
  cat .env
  ```

- **Windows (cmd):**
  ```bash
  type .env
  ```

### Conteúdo do Arquivo `.env`

O arquivo `.env` deverá conter as seguintes variáveis:

```
DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
SECRET_KEY="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Essas variáveis serão usadas para a conexão com o banco de dados e para a autenticação JWT.

3. Suba a aplicação com o Docker Compose:
   ```bash
   docker compose up --build
   ```

   Ou, se não precisar reconstruir os containers:
   ```bash
   docker compose up
   ```

## Testes

Para rodar os testes da aplicação, você deve estar na pasta raiz do projeto (a pasta luizalabs), e não dentro de subpastas como luizalabs/luizalabs. Execute os seguintes comandos na pasta raiz:

```bash
poetry shell
poetry install
task test
```

Isso executará os testes e gerará um relatório de cobertura de código.

### Acessando o Relatório de Cobertura de Código

Após rodar os testes com cobertura, um relatório em HTML será gerado na pasta `htmlcov` no diretório raiz do projeto. Para visualizar o relatório de cobertura, siga os passos abaixo:

1. Navegue até a pasta `htmlcov`:
   ```bash
   cd htmlcov
   ```

2. Abra o arquivo `index.html` no seu navegador preferido. Você pode usar um comando como:

   - **Linux/macOS:**
     ```bash
     xdg-open index.html
     ```

   - **Windows (cmd):**
     ```bash
     start index.html
     ```

O relatório exibirá a cobertura do código-fonte em termos de linhas cobertas por testes e trechos que não foram testados.

## Documentação da API

O **FastAPI** gera automaticamente uma documentação interativa da API no formato Swagger UI, acessível em:

```
http://localhost:8000/docs
```

Nessa interface, você pode visualizar e testar todas as rotas da API.

### Autenticação

Para acessar as rotas protegidas, siga os passos abaixo:

1. Acesse a documentação no Swagger UI (`/docs`).
2. Na interface, vá até a rota `POST /luizalabs/v1/users` e crie um novo usuário.
3. Após criar um usuário, clique no botão **"Authorize"** no canto superior direito da interface Swagger UI.
4. Um pop-up será exibido, onde você deverá inserir suas credenciais:

   - **username**: Seu email.
   - **password**: Sua senha.
   - **client_id** e **client_secret**: Esses campos podem ser ignorados, pois utilizamos apenas `username` e `password`.

---