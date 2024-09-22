import pytest

from luizalabs.controlers.auth import AuthService
from luizalabs.schemas.user import UserSchemaPublic
from tests.factories import UserFactory


@pytest.fixture
def user(session):
    password = '123abc'
    hash_password = AuthService().get_password_hash(password)
    user_instance = UserFactory(password=hash_password)
    session.add(user_instance)
    session.commit()
    user_dict = UserSchemaPublic.model_validate(user_instance).model_dump()
    user_dict['clean_password'] = password

    return user_dict


@pytest.fixture
def other_user(session):
    password = '123abc'
    hash_password = AuthService().get_password_hash(password)
    user_instance = UserFactory(password=hash_password)
    session.add(user_instance)
    session.commit()
    user_dict = UserSchemaPublic.model_validate(user_instance).model_dump()
    return user_dict


@pytest.fixture
def list_users(session):
    users = UserFactory.build_batch(10)
    session.add_all(users)
    session.commit()

    users = [
        UserSchemaPublic.model_validate(user).model_dump() for user in users
    ]

    return users
