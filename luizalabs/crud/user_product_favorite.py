from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select

from luizalabs.models.product import Product
from luizalabs.models.user_product_favorite import UserProductFavorites


class UserProductFavoriteCRUD:
    def __init__(self, session):
        self.session = session

    def get_all_product_favorites(self, user_id: int):
        stmt = (
            select(Product)
            .join(UserProductFavorites, 
                  UserProductFavorites.product_id == Product.id)
            .where(UserProductFavorites.user_id == user_id)
        )
        return paginate(self.session, stmt)

    def get_user_product_favorite(self, user_id: int, product_id: int):
        stmt = select(UserProductFavorites).where(
            UserProductFavorites.user_id == user_id,
            UserProductFavorites.product_id == product_id,
        )
        product_favorite = self.session.scalars(stmt).one_or_none()
        return product_favorite
