
---

# Projeto API LuizaLabs

Este projeto é uma API construída com **FastAPI** para gerenciar o fluxo de favoritar produtos. A API permite:

- CRUD de usuários.
- Listagem de produtos.
- Listagem de produtos favoritos.
- Criação e remoção de produtos favoritos para usuários autenticados.

A aplicação utiliza **SQLAlchemy** para interação com o banco de dados, **JWT** para autenticação e autorização, e **Docker** para simplificar a execução do ambiente.

## Dependências Principais

- **Python**: ^3.12 - Linguagem de programação principal utilizada.
- **FastAPI**: ^0.115.0 - Framework web de alta performance para construção de APIs. Ele também gera automaticamente a documentação da API, acessível via `/docs`.
- **SQLAlchemy**: ^2.0.35 - Biblioteca ORM utilizada para interagir com o banco de dados de maneira eficiente.
- **Pydantic Settings**: ^2.5.2 - Utilizada para gerenciar e validar as configurações do projeto.
- **Pwdlib**: ^0.2.1 (com Argon2) - Biblioteca para hash seguro de senhas.
- **PyJWT**: ^2.9.0 - Utilizada para geração e validação de tokens JWT, essenciais para autenticação e autorização de usuários.
- **FastAPI Pagination**: ^0.12.27 - Facilita a implementação de paginação nas respostas da API.
- **Psycopg**: ^3.2.2 - Driver para comunicação com bancos de dados PostgreSQL.

### Dependências de Desenvolvimento

- **pytest-cov**: ^5.0.0 - Ferramenta para execução de testes com relatório de cobertura.
- **taskipy**: ^1.13.0 - Facilitador para execução de tarefas automáticas.
- **ruff**: ^0.6.5 - Linter para garantir a qualidade do código Python.
- **httpx**: ^0.27.2 - Cliente HTTP para realizar requisições durante os testes.
- **pytest**: ^8.3.3 - Framework de testes para Python.
- **testcontainers**: ^4.8.1 - Utilizado para criar containers temporários em testes.
- **factory-boy**: ^3.3.1 - Facilita a criação de objetos para testes.
- **faker**: ^29.0.0 - Gera dados fictícios para auxiliar nos testes.
- **freezegun**: ^1.5.1 - Permite "congelar" o tempo durante os testes, útil para testes relacionados a data/hora.

## Requisitos

- **Docker**
- **Poetry**

Você deve ter o Docker e o Poetry instalados para rodar o projeto.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd luizalabs
   ```

2. Crie o arquivo `.env` na raiza do repositório, com as seguintes variáveis de ambiente:
   ```bash
   touch luizalabs/.env
   ```

   Adicione as seguintes variáveis ao arquivo `.env`:

   ```
   DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
   SECRET_KEY="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   ALGORITHM="HS256"
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

   - **DATABASE_URL**: Define a URL de conexão com o banco de dados PostgreSQL.
   - **SECRET_KEY**: Utilizada para assinar os tokens JWT.
   - **ALGORITHM**: Algoritmo utilizado para a assinatura dos tokens JWT.
   - **ACCESS_TOKEN_EXPIRE_MINUTES**: Define o tempo de expiração dos tokens de acesso.

3. Suba a aplicação com o Docker Compose:
   ```bash
   docker compose up --build
   ```

   Ou, se não precisar reconstruir os containers:
   ```bash
   docker compose up
   ```

## Testes

Para rodar os testes da aplicação:

```bash
poetry shell
task test
```

Isso executará os testes e gerará um relatório de cobertura de código.

### Acessando o Relatório de Cobertura de Código

Após rodar os testes com cobertura, um relatório em HTML será gerado na pasta `htmlcov` no diretório raiz do projeto. Para visualizar o relatório de cobertura, siga os passos abaixo:

1. Navegue até a pasta `htmlcov`:
   ```bash
   cd htmlcov
   ```

2. Abra o arquivo `index.html` no seu navegador preferido. Você pode abrir diretamente no navegador utilizando um comando como:
   ```bash
   xdg-open index.html  # para Linux
   start index.html     # para Windows
   open index.html      # para macOS
   ```

O relatório exibirá a cobertura do código-fonte em termos de linhas cobertas por testes e trechos que não foram testados.

## Documentação da API

O **FastAPI** gera automaticamente uma documentação interativa da API no formato Swagger UI, que pode ser acessada em:

```
http://localhost:8000/docs
```

Nessa interface, você pode visualizar e testar todas as rotas da API.

### Autenticação

Para acessar as rotas protegidas, siga os passos abaixo:

1. Acesse a documentação no Swagger UI (`/docs`).
2. Na interface, vá até a rota `POST /luizalabs/v1/users` e crie um novo usuário.

3. Após criar um usuário, clique no botão **"Authorize"** no canto superior direito da interface Swagger UI.
4. Um pop-up será exibido (como mostrado na imagem abaixo), onde você deverá inserir suas credenciais:


   - **username**: Seu email.
   - **password**: Sua senha.
   - **client_id** e **client_secret**: Esses campos podem ser ignorados, pois utilizamos apenas `username` e `password`.

5. Após preencher as informações, clique em **"Authorize"**. Uma vez autenticado, você poderá acessar as rotas protegidas da API diretamente pela interface.


---
