from rest_framework import serializers

from app.models import Picture, Shop, Category, Product


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        exclude = ['id', ]


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = ['id', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['parent', 'lft', 'rght', 'tree_id', 'level']


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'parent', 'lft', 'rght', 'tree_id', 'level']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id', ]
