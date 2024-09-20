from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchemaPublic(BaseModel):
    id: int
    username: str
    email: str
    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
