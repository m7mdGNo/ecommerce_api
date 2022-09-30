from itertools import product
from tkinter import FLAT
from django.db import models
from django.conf import settings  
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.db.models import Sum,Max,Min

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=400,null=True,blank=True)
    img = models.ImageField(upload_to='product_imgs')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"{self.name}"


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.name.name)

class Cart(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,unique=True)
    total = models.FloatField(default=0.00)
    order_items = models.ManyToManyField(Item,null=True,blank=True)

    def __str__(self) -> str:
        return f'cart'

@receiver(post_save, sender=User)
def cart_create(sender, instance=None, created=False, **kwargs):
    if created:
        Cart.objects.create(created_by=instance)
    
# @receiver(post_save,sender=Cart)
# def update_cart_total(sender,instance,created,**kwargs):
#     if not created:
#         cart = instance
#         user = cart.created_by.id
#         cart = Cart.objects.filter(created_by=user)
#         cart = cart.annotate(total_price=Sum('order_items__name__price')).get()
#         print(cart.total_price)
        
   