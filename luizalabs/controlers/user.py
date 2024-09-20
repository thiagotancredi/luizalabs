from http import HTTPStatus

from fastapi import HTTPException

from luizalabs.controlers.auth import AuthService
from luizalabs.crud.user import UserCRUD
from luizalabs.models.user import User
from luizalabs.utils.unit_of_work import UnitOfWork


class UserController(UserCRUD):
    def __init__(self, session):
        super().__init__(session)
        self.session: session

    def add_user(self, payload):
        user_email_exists = self.get_user_by_email(payload.email)

        if user_email_exists:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

        payload.password = AuthService().get_password_hash(payload.password)
        new_user = User(**payload.dict())

        with UnitOfWork(self.session):
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)

        return new_user

    def list_users(self):
        list_of_users = self.get_all_users()
        return list_of_users

    def get_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='User not found'
            )
        return user

    def edit_user(self, user_id, user_logged, payload):
        if user_logged.id != user_id:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        with UnitOfWork(self.session):
            user_logged.username = payload.username
            user_logged.email = payload.email
            user_logged.password = AuthService().get_password_hash(
                payload.password
            )

            self.session.commit()
            self.session.refresh(user_logged)

        return user_logged

    def remove_user(self, user_id, user_logged):
        if user_logged.id != user_id:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        with UnitOfWork(self.session):
            self.session.delete(user_logged)
            self.session.commit()
