from typing import List

from pydantic import BaseModel

from luizalabs.schemas.product import ProductSchemaPublic


class UserProductFavoriteSchema(BaseModel):
    product_id: int


class ToggleFavoriteSchemaPublic(BaseModel):
    message: str
