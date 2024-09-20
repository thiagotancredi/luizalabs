from types import TracebackType
from typing import Optional, Type

from sqlalchemy.orm import Session


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[Exception],
        exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        if exc_val:
            self.session.rollback()
        return False
