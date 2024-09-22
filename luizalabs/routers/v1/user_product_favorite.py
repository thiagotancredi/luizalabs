from http import HTTPStatus

from fastapi import APIRouter
from fastapi_pagination import Page

from luizalabs.controlers.user_product_favorite import (
    UserProductFavoriteController,
)
from luizalabs.schemas.product import ProductSchemaPublic
from luizalabs.schemas.user_product_favorite import (
    ToggleFavoriteSchemaPublic,
    UserProductFavoriteSchema,
)
from luizalabs.utils.common_annotations import (
    T_Session,
)
from luizalabs.utils.user_annotations import T_UserLogged

router = APIRouter()


@router.patch(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=ToggleFavoriteSchemaPublic,
    summary='This route adds or removes the product from favorites',
)
def toggle_favorite(
    payload: UserProductFavoriteSchema,
    session: T_Session,
    user_logged: T_UserLogged,
):
    msg = UserProductFavoriteController(session).toggle_favorite(
        user_logged, payload
    )
    return {'message': msg}


@router.get('/', response_model=Page[ProductSchemaPublic])
def product_favorites(session: T_Session, user_logged: T_UserLogged):
    products_favorite = UserProductFavoriteController(
        session
    ).list_products_favorites(user_logged)
    return products_favorite
