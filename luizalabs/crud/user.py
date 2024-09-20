from sqlalchemy import select

from luizalabs.models.user import User


class UserCRUD:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        users_db = self.session.scalars(select(User)).all()
        return users_db

    def get_user_by_email(self, email):
        user_db = self.session.scalar(select(User).where(User.email == email))

        return user_db

    def get_user_by_id(self, user_id: int):
        stmt = select(User).where(User.id == user_id)
        user_db = self.session.execute(stmt).scalar_one_or_none()
        return user_db
