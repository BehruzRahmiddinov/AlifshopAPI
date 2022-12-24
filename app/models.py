import uuid

from django.db.models import UUIDField, CASCADE, ImageField, CharField, DecimalField, ForeignKey, Model
from mptt.fields import TreeForeignKey


class Shop(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    picture = ImageField(upload_to='shop/')
    description = CharField(max_length=500)

    class Meta:
        verbose_name = 'dokon'
        verbose_name_plural = 'dokonlar'

    def __str__(self):
        return self.name


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    subCategory = TreeForeignKey('self', CASCADE, null=True)

    def __str__(self):
        return self.name


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=12, decimal_places=2)
    description = CharField(max_length=500)
    category = ForeignKey(Category, CASCADE)
    shop = ForeignKey(Shop, CASCADE)

    class Meta:
        verbose_name = 'mahsulot'
        verbose_name_plural = 'mahsulotlar'

    def __str__(self):
        return self.name


class Picture(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    picture = ImageField(upload_to='product/%y/%m/%d')
    product = ForeignKey('app.Product', CASCADE)

    class Meta:
        verbose_name = 'rasm'
        verbose_name_plural = 'rasmlar'
