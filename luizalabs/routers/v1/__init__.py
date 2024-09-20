from fastapi import APIRouter

from .auth import router as auth_router
from .product import router as product_route
from .user import router as user_router
from .user_product_favorite import router as user_product_favorite_router

v1_routers = APIRouter(prefix='/luizalabs/v1')

v1_routers.include_router(auth_router, prefix='/auth', tags=['auth'])
v1_routers.include_router(user_router, prefix='/users', tags=['user'])
v1_routers.include_router(product_route, prefix='/products', tags=['product'])
v1_routers.include_router(
    user_product_favorite_router,
    prefix='/user_product_favorite_router',
    tags=['User Product Favorite'],
)
