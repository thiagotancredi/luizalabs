import pytest

from luizalabs.schemas.product import ProductSchemaPublic
from tests.factories import ProductFactory


@pytest.fixture
def product(session):
    product_instance = ProductFactory()
    session.add(product_instance)
    session.commit()
    product_dict = ProductSchemaPublic.model_validate(
        product_instance
    ).model_dump()

    return product_dict


@pytest.fixture
def list_products(session):
    products = ProductFactory.build_batch(10)
    session.add_all(products)
    session.commit()

    products = [
        ProductSchemaPublic.model_validate(product).model_dump()
        for product in products
    ]

    return products
