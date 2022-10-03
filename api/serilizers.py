from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import Product,Brand,Category,Cart,Item,wishlist,wishlist_items
from django.contrib.auth.models import User

class UpdateProdcutSerializer(ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('discount', )

class ProdcutSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProdcutAddDiscountSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['discount']

class CategorySerializer(ModelSerializer):
    num_of_products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
    
    def get_num_of_products(self,object):
        if hasattr(object,'num_of_products'):
            return object.num_of_products
        return object.product_set.count()

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CreateItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
    def save(self,**kwargs):
        user = self.validated_data['user']
        cart = Cart.objects.get(created_by=user)
        super_return = super().save(**kwargs)
        id = self.instance.id
        item = Item.objects.filter(user=user).get(id=id)
        cart.order_items.add(item)
        cart.save()
        return super_return

class CartSerializer(ModelSerializer):
    order_items = CreateItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class DeleteItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
class Add_item_to_wishlistSerializer(ModelSerializer):
    class Meta:
        model = wishlist_items
        fields = '__all__'
    
    def save(self, **kwargs):
        user = self.validated_data['user']
        wish_list = wishlist.objects.get(user=user)
        super_return = super().save(**kwargs)
        id = self.instance.id
        item = wishlist_items.objects.filter(user=user).get(id=id)
        wish_list.items.add(item)
        wish_list.save()
        return super_return

class WishListSerializer(ModelSerializer):
    class Meta:
        model = wishlist
        fields = '__all__'