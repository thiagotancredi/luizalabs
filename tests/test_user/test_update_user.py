from http import HTTPStatus

from tests import BASE_URL_USER
from tests.factories import UserFactory


def test_update_user(client, authenticated_user):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']
    new_data_user = UserFactory()

    expected_response_data = {
        'id': 1,
        'username': new_data_user.username,
        'email': new_data_user.email,
    }

    response = client.put(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
        json={
            'username': new_data_user.username,
            'email': new_data_user.email,
            'password': new_data_user.password,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response_data


def test_update_user_without_permissions(
    client, authenticated_user, other_user
):
    other_user_id = other_user['id']
    access_token = authenticated_user['access_token']

    new_data_user = UserFactory()

    response = client.put(
        f'{BASE_URL_USER}{other_user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
        json={
            'username': new_data_user.username,
            'email': new_data_user.email,
            'password': new_data_user.password,
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_update_user_without_username(client, authenticated_user):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']
    new_data_user = UserFactory()

    payload = {
        'email': new_data_user.email,
        'password': new_data_user.password,
    }
    response = client.put(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
        json=payload,
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'username']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert (
        response.json()['detail'][0]['input']['email'] == new_data_user.email
    )
    assert (
        response.json()['detail'][0]['input']['password']
        == new_data_user.password
    )


def test_update_user_without_email(client, authenticated_user):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']
    new_data_user = UserFactory()

    payload = {
        'username': new_data_user.username,
        'password': new_data_user.password,
    }
    response = client.put(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
        json=payload,
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'email']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert (
        response.json()['detail'][0]['input']['username']
        == new_data_user.username
    )
    assert (
        response.json()['detail'][0]['input']['password']
        == new_data_user.password
    )


def test_update_user_without_password(client, authenticated_user):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']
    new_data_user = UserFactory()

    payload = {
        'username': new_data_user.username,
        'email': new_data_user.email,
    }
    response = client.put(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
        json=payload,
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['type'] == 'missing'
    assert response.json()['detail'][0]['loc'] == ['body', 'password']
    assert response.json()['detail'][0]['msg'] == 'Field required'
    assert (
        response.json()['detail'][0]['input']['username']
        == new_data_user.username
    )
    assert (
        response.json()['detail'][0]['input']['email'] == new_data_user.email
    )
