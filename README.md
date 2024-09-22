# Projeto LuizaLabs

Este projeto é uma API construída com **FastAPI**, utilizando **SQLAlchemy** para interação com o banco de dados, **JWT** para autenticação e autorização, e **Docker** para facilitar a execução do ambiente de desenvolvimento.

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

Você deve ter o Docker e o Poetry instalados no seu sistema.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/thiagotancredi/luizalabs.git
   cd luizalabs
   ```

2. Suba a aplicação com o Docker Compose:
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

## Documentação da API

O **FastAPI** gera automaticamente uma documentação interativa da API no formato Swagger UI, que pode ser acessada em:

```
http://localhost:8000/docs
```

Nessa interface, você pode visualizar e testar todas as rotas da API.

### Autenticação

Para acessar as rotas protegidas, você precisará se autenticar utilizando o fluxo OAuth2 com Password Bearer. Siga os passos abaixo:

1. Acesse a documentação no Swagger UI.
2. Clique no botão **"Authorize"** no canto superior direito.
3. Um pop-up será exibido (como mostrado na imagem abaixo), onde você deverá inserir suas credenciais.

- **username**: Seu email.
- **password**: Sua senha.
- **client_id** e **client_secret**: Esses campos podem ser ignorados, pois utilizamos apenas `username` e `password`.

Após preencher as informações, clique em **"Authorize"**. Uma vez autenticado, você poderá acessar as rotas protegidas da API diretamente pela interface.
