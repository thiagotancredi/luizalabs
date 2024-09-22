from http import HTTPStatus
from freezegun import freeze_time


from tests import BASE_URL_AUTH, BASE_URL_USER
from tests.factories import UserFactory

def test_generate_auth_token(client, user):
    response = client.post(
        f'{BASE_URL_AUTH}token/',
        data={
            'username': user['email'], 
            'password': user['clean_password']
        },
    )
    token_data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token_data
    assert 'token_type' in token_data


def test_expired_token_rejected(client, user):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            f'{BASE_URL_AUTH}token/',
            data={
                'username': user['email'], 
                'password': user['clean_password']
            },
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']

    with freeze_time('2023-07-14 12:31:00'):
        new_data_user = UserFactory()
        response = client.put(
            f'{BASE_URL_USER}{user['id']}',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'username': new_data_user.username,
                'email': new_data_user.email,
                'password': new_data_user.password,
            },
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}

def test_invalid_user_token(client):
    
    unregistered_user = UserFactory()

    response = client.post(
        f'{BASE_URL_AUTH}token/',
        data={
            'username': unregistered_user.email, 
            'password': unregistered_user.password
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_invalid_password_rejected(client, user):
    incorrect_password = '$6M03w1U'

    response = client.post(
        f'{BASE_URL_AUTH}token/',
        data={
            'username': user['email'], 
            'password': incorrect_password
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_successful_token_refresh(client, authenticated_user):
    valid_token = authenticated_user['access_token']
    response = client.post(
        f'{BASE_URL_AUTH}refresh_token/',
        headers={'Authorization': f'Bearer {valid_token}'},
    )

    refreshed_data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in refreshed_data
    assert 'token_type' in refreshed_data
    assert refreshed_data['token_type'] == 'bearer'


def test_expired_token_refresh_rejected(client, user):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            f'{BASE_URL_AUTH}token/',
            data={
                'username': user['email'], 
                'password': user['clean_password']
            },
        )
        assert response.status_code == HTTPStatus.OK
        token = response.json()['access_token']

    with freeze_time('2023-07-14 12:31:00'):
        response = client.post(
            f'{BASE_URL_AUTH}refresh_token/',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}