from fastapi import APIRouter
from fastapi_pagination import Page

from luizalabs.controlers.product import ProductController
from luizalabs.schemas.product import ProductSchemaPublic
from luizalabs.utils.common_annotations import (
    T_Session,
)

router = APIRouter()


@router.get('/', response_model=Page[ProductSchemaPublic])
def read_products(session: T_Session):
    db_products = ProductController(session).list_products()
    return db_products


@router.get('/{product_id}', response_model=ProductSchemaPublic)
def read_product(session: T_Session, product_id: int):
    db_product = ProductController(session).get_product(product_id)
    return db_product
