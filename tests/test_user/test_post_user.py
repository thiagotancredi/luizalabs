from http import HTTPStatus

from tests import BASE_URL_USER
from tests.factories import UserFactory


def test_create_user(client):
    new_user = UserFactory()

    payload = {
        'username': new_user.username,
        'email': new_user.email,
        'password': new_user.password,
    }
    expected_response_data = {
        'id': 1,
        'username': new_user.username,
        'email': new_user.email,
    }

    response = client.post(BASE_URL_USER, json=payload)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == expected_response_data


def test_create_user_email_already_exists(client, user):
    new_user = UserFactory()
    payload = {
        'username': new_user.username,
        'email': user['email'],
        'password': new_user.password,
    }

    response = client.post(BASE_URL_USER, json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert 'detail' in response.json()
    assert response.json() == {'detail': 'Email already exists'}


def test_create_user_without_username(client):
    new_user = UserFactory.build()
    payload = {
        'email': new_user.email,
        'password': new_user.password,
    }

    response = client.post(BASE_URL_USER, json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'username']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert response.json()['detail'][0]['input']['email'] == new_user.email
    assert (
        response.json()['detail'][0]['input']['password'] == new_user.password
    )


def test_create_user_without_email(client):
    new_user = UserFactory.build()
    payload = {
        'username': new_user.username,
        'password': new_user.password,
    }

    response = client.post(BASE_URL_USER, json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'email']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert (
        response.json()['detail'][0]['input']['username'] == new_user.username
    )
    assert (
        response.json()['detail'][0]['input']['password'] == new_user.password
    )


def test_create_user_without_password(client):
    new_user = UserFactory.build()
    payload = {'username': new_user.username, 'email': new_user.email}

    response = client.post(BASE_URL_USER, json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'password']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert (
        response.json()['detail'][0]['input']['username'] == new_user.username
    )
    assert response.json()['detail'][0]['input']['email'] == new_user.email
