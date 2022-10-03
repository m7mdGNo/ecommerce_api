from django.contrib import admin
from .models import Category,Product,Brand,Cart,Item,wishlist,wishlist_items
from django.contrib.auth.admin import UserAdmin


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Item)

class WishListAdminConfig(admin.ModelAdmin):
    list_display = ('created_by',)

admin.site.register(wishlist,WishListAdminConfig)

class WishListItemsAdminConfig(admin.ModelAdmin):
    list_display = ('user','name')

admin.site.register(wishlist_items)
 
class CartAdminConfig(admin.ModelAdmin):
    list_display = ('created_by','total')

admin.site.register(Cart,CartAdminConfig)