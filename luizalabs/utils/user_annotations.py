from typing import Annotated

from fastapi import Depends

from luizalabs.controlers.auth import AuthService
from luizalabs.models.user import User
from luizalabs.utils.common_annotations import T_AuthToken, T_Session


def get_current_user(session: T_Session, access_token: T_AuthToken):
    auth_service = AuthService()
    user = auth_service.user_logged(session, access_token)
    return user


T_UserLogged = Annotated[User, Depends(get_current_user)]
