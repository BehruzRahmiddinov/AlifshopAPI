from django_filters import rest_framework, NumberFilter, FilterSet

from app.models import Product, Category


class ProductFilter(rest_framework.FilterSet):
    # name = CharFilter(field_name='name', lookup_expr='in')
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name']


class CategoryFilter(FilterSet):
    # name = CharFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Category
        fields = ['name']
