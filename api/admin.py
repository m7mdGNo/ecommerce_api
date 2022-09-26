from django.contrib import admin
from .models import Category,Product,Brand,Cart,Item
# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Item)