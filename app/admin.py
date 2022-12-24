from django.contrib import admin

from app.models import Category, Shop, Product


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class ShopAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shop, ShopAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
