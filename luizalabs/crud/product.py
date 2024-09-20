from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select

from luizalabs.models.product import Product


class ProductCRUD:
    def __init__(self, session):
        self.session = session

    def get_all_products(self):
        stmt = select(Product)
        return paginate(self.session, stmt)

    def get_product_by_id(self, product_id: int):
        stmt = select(Product).where(Product.id == product_id)
        product = self.session.execute(stmt).scalar_one_or_none()
        return product
