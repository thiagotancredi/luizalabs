#!/bin/sh




# Executa as migrações do banco de dados
poetry run alembic upgrade head

# Insere produtos na tabela
poetry run python luizalabs/seeds/product_seed.py

# Inicia a aplicação
poetry run uvicorn --host 0.0.0.0 --port 8000 luizalabs.app:app