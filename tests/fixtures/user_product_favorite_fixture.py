import pytest
from sqlalchemy import select

from luizalabs.models.product import Product
from luizalabs.models.user_product_favorite import UserProductFavorites
from luizalabs.schemas.product import ProductSchemaPublic

@pytest.fixture
def product_favorite(session, authenticated_user, product):
    user_id = authenticated_user['user']['id']
    product_id = product['id']

    user_product_favorite = UserProductFavorites(
        user_id=user_id, 
        product_id=product_id
    )

    session.add(user_product_favorite)
    session.commit()

    stmt = select(Product).where(Product.id == product_id)
    product_db = session.execute(stmt).scalar_one_or_none()

    product = ProductSchemaPublic.model_validate(
        product_db
    ).model_dump()

    return product

@pytest.fixture
def list_products_favorite(session, authenticated_user, list_products):
    user_id = authenticated_user['user']['id']
    
    user_product_favorites = [
        UserProductFavorites(user_id=user_id, product_id=product['id'])
        for product in list_products
    ]

    session.add_all(user_product_favorites)
    session.commit()

    stmt = (
        select(Product)
        .join(UserProductFavorites, 
              UserProductFavorites.product_id == Product.id)
        .where(UserProductFavorites.user_id == user_id)
    )
    
    products_db = session.execute(stmt).scalars().all()
    
    list_product_favorite = [
        ProductSchemaPublic.model_validate(product).model_dump()
        for product in products_db
    ]

    return list_product_favorite
