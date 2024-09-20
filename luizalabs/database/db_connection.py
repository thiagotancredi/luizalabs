from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from luizalabs.settings.settings import Settings

database_url = Settings().DATABASE_URL

engine = create_engine(database_url)


def get_session():
    with Session(engine) as session:
        yield session
