import pytest


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