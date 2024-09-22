from http import HTTPStatus

from tests import BASE_URL_USER_PRODUCT_FAVORITE, EXPECTED_TOTAL


def test_list_favorites_products(
        client, 
        authenticated_user, 
        list_products_favorite
):
    expected_page = 1
    expected_size = 50
    access_token = authenticated_user['access_token']

    response = client.get(
        BASE_URL_USER_PRODUCT_FAVORITE,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products_favorite


def test_list_favorites_products_paginate(
        client, 
        authenticated_user, 
        list_products_favorite
):
    expected_page = 1
    expected_size = 5
    access_token = authenticated_user['access_token']

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=1&size=5',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products_favorite[:5]
    assert response.json()['items'][0]['id'] == list_products_favorite[0]['id']


def test_list_favorites_products_page_2(
        client, 
        authenticated_user, 
        list_products_favorite
):
    expected_page = 2
    expected_size = 5
    access_token = authenticated_user['access_token']

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=2&size=5',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products_favorite[-5:]
    assert response.json()['items'][0]['id'] == list_products_favorite[5]['id']


def test_list_favorites_products_empty(client, authenticated_user):

    access_token = authenticated_user['access_token']

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=2&size=5',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['total'] == 0
    assert response.json()['items'] == []


def test_list_favorites_products_page_out_of_range(
        client, 
        authenticated_user,
        list_products_favorite
):
    
    expected_page = 10
    expected_size = 5

    access_token = authenticated_user['access_token']

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=10&size=5',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == []


def test_list_favorites_products_invalid_page_params(
        client, 
        authenticated_user
):
    access_token = authenticated_user['access_token']

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=abc&size=5',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['loc'] == ['query', 'page']
    assert (
        response.json()['detail'][0]['msg'] == 'Input should be '
        'a valid integer, unable to parse string as an integer'
    )
    assert response.json()['detail'][0]['type'] == 'int_parsing'
    assert response.json()['detail'][0]['input'] == 'abc'


def test_list_favorites_products_invalid_size_params(
        client,
        authenticated_user
):

    access_token = authenticated_user['access_token']
    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=1&size=abc',
        headers={'Authorization': f'Bearer {access_token}'}
    
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['loc'] == ['query', 'size']
    assert (
        response.json()['detail'][0]['msg'] == 'Input should be '
        'a valid integer, unable to parse string as an integer'
    )
    assert response.json()['detail'][0]['type'] == 'int_parsing'
    assert response.json()['detail'][0]['input'] == 'abc'


def test_list_favorites_products_unauthenticated_user(
        client
):

    response = client.get(
        f'{BASE_URL_USER_PRODUCT_FAVORITE}?page=1&size=abc',
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}