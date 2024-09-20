from fastapi import APIRouter

from .auth import router as auth_router
from .user import router as user_router

v1_routers = APIRouter(prefix='/luizalabs/v1')

v1_routers.include_router(user_router, prefix='/user', tags=['user'])
v1_routers.include_router(auth_router, prefix='/auth', tags=['auth'])
