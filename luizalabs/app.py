from fastapi import FastAPI
from fastapi_pagination import add_pagination

from luizalabs.routers.v1 import v1_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title='LuizaLabs', version='0.1.0', description='Teste Api LuizaLabs'
    )
    app.include_router(v1_routers)
    add_pagination(app)

    return app


app = create_app()
