from django.contrib import admin
from .models import Product, Offer, Categories


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')


admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


admin.site.register(Offer, OfferAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url')


admin.site.register(Categories, CategoriesAdmin)










