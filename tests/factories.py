import random

import factory
from faker import Faker

from luizalabs.models.product import Product
from luizalabs.models.user import User

fake = Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.name())
    email = factory.LazyAttribute(
        lambda obj: (
            f'{obj.username.strip().replace(" ", "").lower()}@email.com'
        )
    )
    password = factory.LazyAttribute(lambda _: fake.password())


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    title = factory.LazyAttribute(lambda _: fake.word())
    price = factory.LazyAttribute(
        lambda _: fake.pyfloat(left_digits=3, right_digits=2, positive=True)
    )
    image = factory.LazyAttribute(lambda _: fake.image_url())
    brand = factory.LazyAttribute(lambda _: fake.company())
    reviewScore = factory.LazyAttribute(
        lambda _: round(random.uniform(1.0, 5.0), 1)
    )
