import django_filters
from rest_framework import viewsets

from app.filter import CategoryFilter, ProductFilter
from app.models import Product, Category, Shop
from app.serializer import ProductSerializer, CategorySerializer, ShopSerializer, CreateCategorySerializer


class ProductVIewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ProductFilter


class CategoryVIewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CategoryFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCategorySerializer
        return super().get_serializer_class()


class ShopVIewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
