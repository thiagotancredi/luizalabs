from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_pagination import Params
from sqlalchemy.orm import Session

from luizalabs.database.db_connection import get_session

T_Session = Annotated[Session, Depends(get_session)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
T_ParamsPagination = Annotated[Params, Depends()]

T_AuthToken = Annotated[
    str, Depends(OAuth2PasswordBearer(tokenUrl='/luizalabs/v1/auth/token'))
]
