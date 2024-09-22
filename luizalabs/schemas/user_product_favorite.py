from pydantic import BaseModel


class UserProductFavoriteSchema(BaseModel):
    product_id: int


class ToggleFavoriteSchemaPublic(BaseModel):
    message: str
