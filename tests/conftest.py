import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from luizalabs.app import app
from luizalabs.database.db_connection import get_session
from luizalabs.database.orm_registry import table_mapper


@pytest.fixture(scope='session')
def engine():
    with PostgresContainer('postgres:16', driver='psycopg') as postgres:
        __engine = create_engine(postgres.get_connection_url())
        with __engine.begin():
            yield __engine


@pytest.fixture
def session(engine):
    table_mapper.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        session.rollback()

    table_mapper.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_overrride():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_overrride
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def authenticated_user(client, user):
    response = client.post(
        'luizalabs/v1/auth/token',
        data={
            'username': user['email'],
            'password': user['clean_password'],
        },
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )

    access_token = response.json()['access_token']
    token_type = response.json()['token_type']

    return {
        'user': user,
        'access_token': access_token,
        'token_type': token_type,
    }


pytest_plugins = [
    "tests.fixtures.product_fixture",
    "tests.fixtures.user_fixture",
]