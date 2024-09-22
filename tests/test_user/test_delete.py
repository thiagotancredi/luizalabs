from http import HTTPStatus

from tests import BASE_URL_USER


def test_delete_user(client, authenticated_user):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']

    response = client.delete(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    get_response = client.get(f'{BASE_URL_USER}{user_id}')

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert get_response.json() == {'detail': 'User not found'}


def test_delete_user_with_favorited_products(
        client, 
        authenticated_user, 
        product_favorite
):
    user_id = authenticated_user['user']['id']
    access_token = authenticated_user['access_token']

    response = client.delete(
        f'{BASE_URL_USER}{user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    get_response = client.get(f'{BASE_URL_USER}{user_id}')

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert get_response.status_code == HTTPStatus.NOT_FOUND
    assert get_response.json() == {'detail': 'User not found'}


def test_delete_user_without_permissions(
    client, authenticated_user, other_user
):
    other_user_id = other_user['id']
    access_token = authenticated_user['access_token']

    response = client.delete(
        f'{BASE_URL_USER}{other_user_id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_unauthenticated_user(
    client, 
    authenticated_user
):
    user_id = authenticated_user['user']['id']
    response = client.delete(
        f'{BASE_URL_USER}{user_id}',
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}