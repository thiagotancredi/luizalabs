from pydantic import BaseModel, ConfigDict


class ProductSchemaPublic(BaseModel):
    id: int
    title: str
    price: float
    image: str
    brand: str
    reviewScore: float
    model_config = ConfigDict(from_attributes=True)
