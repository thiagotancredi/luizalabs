from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from luizalabs.database.orm_registry import table_mapper


@table_mapper.mapped_as_dataclass
class UserProductFavorites:
    __tablename__ = 'user_product_favorites'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id'), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
