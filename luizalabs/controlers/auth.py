import datetime
from http import HTTPStatus

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError, decode, encode
from pwdlib import PasswordHash
from zoneinfo import ZoneInfo

from luizalabs.crud.user import UserCRUD
from luizalabs.schemas.security import TokenDataSchema
from luizalabs.settings.settings import Settings
from luizalabs.utils.common_annotations import T_AuthToken, T_Session

oauth2schema = OAuth2PasswordBearer(tokenUrl='/luizalabs/v1/auth/token')


class AuthService:
    def __init__(self):
        self.pwd_context = PasswordHash.recommended()
        self.settings = Settings()

    def user_logged(self, session: T_Session, access_token: T_AuthToken):
        auth_exception = HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        try:
            payload = decode(
                access_token,
                self.settings.SECRET_KEY,
                algorithms=[self.settings.ALGORITHM],
            )
            user_identifier: str = payload.get('sub')
            if not user_identifier:
                raise auth_exception
            token_info = TokenDataSchema(username=user_identifier)
        except (DecodeError, ExpiredSignatureError):
            raise auth_exception

        user_database = UserCRUD(session).get_user_by_email(
            token_info.username
        )

        if not user_database:
            raise auth_exception

        return user_database

    def generate_access_token(self, token_data: dict):
        token_payload = token_data.copy()
        expiration_time = datetime.datetime.now(
            tz=ZoneInfo('UTC')
        ) + datetime.timedelta(
            minutes=self.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        token_payload.update({'exp': expiration_time})
        jwt_encoded = encode(
            token_payload,
            self.settings.SECRET_KEY,
            algorithm=self.settings.ALGORITHM,
        )
        return jwt_encoded

    def login_for_access_token(self, form_data, session):
        user = UserCRUD(session).get_user_by_email(form_data.username)

        if not user:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Incorrect email or password',
            )

        if not self.verify_password(form_data.password, user.password):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Incorrect email or password',
            )

        access_token = self.generate_access_token(
            token_data={'sub': user.email}
        )
        return {'access_token': access_token, 'token_type': 'bearer'}

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, password: str, hashed_password: str):
        return self.pwd_context.verify(password, hashed_password)
