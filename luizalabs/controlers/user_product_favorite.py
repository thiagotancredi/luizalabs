from http import HTTPStatus

from fastapi import HTTPException

from luizalabs.crud.product import ProductCRUD
from luizalabs.crud.user_product_favorite import UserProductFavoriteCRUD
from luizalabs.models.user_product_favorite import UserProductFavorites
from luizalabs.utils.unit_of_work import UnitOfWork


class UserProductFavoriteController(UserProductFavoriteCRUD, ProductCRUD):
    def __init__(self, session):
        super().__init__(session)
        ProductCRUD.__init__(self, session)
        self.session: session

    def list_products_favorites(self, user_logged):
        list_of_products = self.get_all_product_favorites(user_logged.id)
        return list_of_products

    def remove_favorite(self, user_product_favorite):
        self.session.delete(user_product_favorite)

    def create_favorite(self, payload, user_logged):
        product_favorite = UserProductFavorites(
            user_id=user_logged.id, product_id=payload.product_id
        )
        self.session.add(product_favorite)

    def toggle_favorite(self, user_logged, payload):
        check_exist_product = self.get_product_by_id(payload.product_id)

        if check_exist_product:
            alredy_product_favorite = self.get_user_product_favorite(
                user_logged.id, payload.product_id
            )

            with UnitOfWork(self.session):
                if alredy_product_favorite:
                    self.remove_favorite(alredy_product_favorite)
                    msg = 'Product Removed Successfully'
                elif not alredy_product_favorite:
                    check_exist_product = self.get_product_by_id(
                        payload.product_id
                    )
                    if check_exist_product:
                        self.create_favorite(payload, user_logged)
                        msg = 'Successfully Favorite Product'

                self.session.commit()
        else:
            raise HTTPException(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                detail='Product Not Exists',
            )

        return msg
