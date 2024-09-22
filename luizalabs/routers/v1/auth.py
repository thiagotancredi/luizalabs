from fastapi import APIRouter

from luizalabs.controlers.auth import AuthService
from luizalabs.schemas.security import TokenSchema
from luizalabs.utils.common_annotations import (
    T_AuthToken,
    T_OAuth2Form,
    T_Session,
)

router = APIRouter()


@router.post('/token/', response_model=TokenSchema)
def login_auth_token(formdata: T_OAuth2Form, session: T_Session):
    access_token = AuthService().login_for_access_token(formdata, session)
    return access_token


@router.post('/refresh_token/', response_model=TokenSchema)
def login_auth_refresh_token(access_token: T_AuthToken, session: T_Session):
    auth_service = AuthService()

    user = auth_service.user_logged(session, access_token)

    refresh_token = auth_service.generate_access_token(
        token_data={'sub': user.email}
    )

    return {'access_token': refresh_token, 'token_type': 'bearer'}
