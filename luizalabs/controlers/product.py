from http import HTTPStatus

from fastapi import HTTPException

from luizalabs.crud.product import ProductCRUD


class ProductController(ProductCRUD):
    def __init__(self, session):
        super().__init__(session)
        self.session: session

    def list_products(self):
        list_of_products = self.get_all_products()
        return list_of_products

    def get_product(self, product_id):
        user = self.get_product_by_id(product_id)
        if user is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='Product not found'
            )
        return user
