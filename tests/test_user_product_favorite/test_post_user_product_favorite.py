from http import HTTPStatus
from tests import BASE_URL_USER_PRODUCT_FAVORITE

def test_toggle_add_favorite(client, authenticated_user, product):
    access_token = authenticated_user['access_token']

    payload = {'product_id': product['id']}

    response = client.patch(
        BASE_URL_USER_PRODUCT_FAVORITE, 
        json=payload,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Successfully Favorite Product'}

def test_toggle_remove_favorite(client, authenticated_user, product_favorite):
    access_token = authenticated_user['access_token']

    payload = {'product_id': product_favorite["id"]}

    response = client.patch(
        BASE_URL_USER_PRODUCT_FAVORITE, 
        json=payload,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Product Removed Successfully'}


def test_toggle_add_favorite_nonexistent_product(
        client, 
        authenticated_user
):
    invalid_product_id = 99
    access_token = authenticated_user['access_token']

    payload = {'product_id': invalid_product_id}

    response = client.patch(
        BASE_URL_USER_PRODUCT_FAVORITE, 
        json=payload,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {'detail': 'Product Not Exists'}

def test_toggle_favorite_product_unauthenticated_user(
        client,
        product
):

    payload = {'product_id': product['id']}

    response = client.patch(
        BASE_URL_USER_PRODUCT_FAVORITE, 
        json=payload,
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}