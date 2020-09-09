from django.contrib import admin
from .models import Product, Category, Metal, Theme

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'metal',
        'theme',
        'price',
        'image',
    )

    ordering = ('sku', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class MetalAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Metal, MetalAdmin)
admin.site.register(Theme, ThemeAdmin)
