from http import HTTPStatus

from tests import BASE_URL_PRODUCT, EXPECTED_TOTAL



def test_list_products(client, list_products):
    expected_page = 1
    expected_size = 50

    response = client.get(BASE_URL_PRODUCT)

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products


def test_list_products_paginate(client, list_products):
    expected_page = 1
    expected_size = 5

    response = client.get(f'{BASE_URL_PRODUCT}?page=1&size=5')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products[:5]
    assert response.json()['items'][0]['id'] == list_products[0]['id']


def test_list_products_page_2(client, list_products):
    expected_page = 2
    expected_size = 5

    response = client.get(f'{BASE_URL_PRODUCT}?page=2&size=5')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == list_products[-5:]
    assert response.json()['items'][0]['id'] == list_products[5]['id']


def test_list_product_empty(client):
    response = client.get(f'{BASE_URL_PRODUCT}?page=1&size=5')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['total'] == 0
    assert response.json()['items'] == []


def test_list_product_page_out_of_range(client, list_products):
    expected_page = 10
    expected_size = 5

    response = client.get(f'{BASE_URL_PRODUCT}?page=10&size=5')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['page'] == expected_page
    assert response.json()['size'] == expected_size
    assert response.json()['total'] == EXPECTED_TOTAL
    assert response.json()['items'] == []


def test_list_product_invalid_page_params(client):
    response = client.get(f'{BASE_URL_PRODUCT}?page=abc&size=5')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['loc'] == ['query', 'page']
    assert (
        response.json()['detail'][0]['msg'] == 'Input should be '
        'a valid integer, unable to parse string as an integer'
    )
    assert response.json()['detail'][0]['type'] == 'int_parsing'
    assert response.json()['detail'][0]['input'] == 'abc'


def test_list_product_invalid_size_params(client):
    response = client.get(f'{BASE_URL_PRODUCT}?page=1&size=abc')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['loc'] == ['query', 'size']
    assert (
        response.json()['detail'][0]['msg'] == 'Input should be '
        'a valid integer, unable to parse string as an integer'
    )
    assert response.json()['detail'][0]['type'] == 'int_parsing'
    assert response.json()['detail'][0]['input'] == 'abc'


def test_get_product_by_id(client, product):
    product_id = product['id']
    response = client.get(f'{BASE_URL_PRODUCT}{product_id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == product


def test_get_product_by_nonexistent_id(client):
    nonexistent_id = 99
    response = client.get(f'{BASE_URL_PRODUCT}{nonexistent_id}')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Product not found'}


def test_get_product_by_invalid_id(client):
    product_id = 'abc'
    response = client.get(f'{BASE_URL_PRODUCT}{product_id}')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()['detail'][0]['loc'] == ['path', 'product_id']
    assert (
        response.json()['detail'][0]['msg'] == 'Input should be '
        'a valid integer, unable to parse string as an integer'
    )
    assert response.json()['detail'][0]['type'] == 'int_parsing'
    assert response.json()['detail'][0]['input'] == 'abc'
