from http import HTTPStatus
from fastapi import APIRouter, HTTPException, logger
from fastapi_pagination import Page

from luizalabs.controlers.user import UserController
from luizalabs.schemas.user import UserSchema, UserSchemaPublic
from luizalabs.utils.common_annotations import (
    T_ParamsPagination,
    T_Session,
)
from luizalabs.utils.user_annotations import T_UserLogged



router = APIRouter()


@router.post('/', response_model=UserSchemaPublic)
def create_user(payload: UserSchema, session: T_Session):
    new_user = UserController(session).add_user(payload)
    return new_user


@router.get('/', response_model=Page[UserSchemaPublic])
def read_users(session: T_Session, params: T_ParamsPagination):
    db_users = UserController(session).list_users(params)
    return db_users


@router.get('/{user_id}', response_model=UserSchemaPublic)
def read_user(session: T_Session, user_id: int):
    db_user = UserController(session).get_user(user_id)
    return db_user

@router.put('/{user_id}', response_model=UserSchemaPublic)
def update_user(
    user_id: int,
    payload: UserSchema,
    session: T_Session,
    user_logged: T_UserLogged,
):
    update_user = UserController(session).edit_user(
        user_id, user_logged, payload
    )

    return update_user


@router.delete('/{user_id}', response_model=UserSchemaPublic)
def delete_user(user_id: int, session: T_Session, user_logged: T_UserLogged):
    UserController(session).remove_user(user_id, user_logged)
