from django.contrib import admin
from .models import Product, Category, Metal, Theme

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Metal)
admin.site.register(Theme)
