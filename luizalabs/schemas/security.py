from pydantic import BaseModel


class TokenDataSchema(BaseModel):
    username: str | None = None


class TokenSchema(BaseModel):
    token_type: str
    access_token: str
