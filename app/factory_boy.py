import factory

from app.models import Shop, Category, Product, Picture


class ShopFactory(factory.Factory):
    class Meta:
        model = Shop


class CategoryFactory(factory.Factory):
    class Meta:
        model = Category


class ProductFactory(factory.Factory):
    class Meta:
        model = Product


class PictureFactory(factory.Factory):
    class Meta:
        model = Picture
