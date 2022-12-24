from django.urls import include, path
from rest_framework import routers

from app.views import CategoryVIewSet, ShopVIewSet, ProductVIewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryVIewSet)
router.register(r'shop', ShopVIewSet)
router.register(r'product', ProductVIewSet)

urlpatterns = [
    path('', include(router.urls)),
]
