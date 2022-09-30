from urllib import request
from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from .models import Product,Brand,Category,Cart,Item
from django.contrib.auth.models import User

class ProdcutSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

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
        name = self.validated_data['name']
        qty = self.validated_data['qty']
        cart = Cart.objects.get(created_by=user)
        product = Product.objects.get(name=name)
        price = product.price
        cart.total += qty*price
        super().save(**kwargs)
        id = self.instance.id
        item = Item.objects.filter(user=user).get(id=id)
        cart.order_items.add(item)
        cart.save()

        return super().save(**kwargs)

class CartSerializer(ModelSerializer):
    order_items = CreateItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class DeleteItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
    def save(self,**kwargs):
        user = self.validated_data['user']
        name = self.validated_data['name']
        cart = Cart.objects.get(created_by=user)
        # cart.order_items.all().
        product = Product.objects.get(name=name)
        price = product.price
        print(price)
        cart.total -= price
        cart.save()

        return super().save(**kwargs)
    