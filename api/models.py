from email.policy import default
from enum import unique
from itertools import product
from django.db import models
from django.conf import settings  
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.db.models import Sum,Max,Min
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    is_seller = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    price_after_discount = models.FloatField(default=0)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(max_length=400,null=True,blank=True)
    img = models.ImageField(upload_to='product_imgs')
    discount = models.IntegerField(default=0)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"{self.name}"


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.name.name)

class Cart(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    total = models.FloatField(default=0.00)
    order_items = models.ManyToManyField(Item,null=True,blank=True)

    def __str__(self) -> str:
        return f'cart'

class wishlist_items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.name

class wishlist(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    order_items = models.ManyToManyField(wishlist_items,null=True,blank=True)

    def __str__(self) -> str:
        return f'cart'

@receiver(post_save, sender=User)
def wishlist_create(sender, instance=None, created=False, **kwargs):
    if created:
        wishlist.objects.create(created_by=instance)

@receiver(post_save, sender=User)
def cart_create(sender, instance=None, created=False, **kwargs):
    if created:
        Cart.objects.create(created_by=instance)

@receiver(post_save, sender=Product)
def dicount_price_filed(sender,instance,created,**kwargs):
    if created:
        instance.price_after_discount = instance.price
        instance.save()

# @receiver(pre_save, sender=Product)
# def update_dicount_price_filed(sender,instance,**kwargs):
#     discount = instance.price-(instance.price*(instance.discount/100))
#     if instance.price_after_discount != discount:
#         instance.price_after_discount = discount
#         instance.save()
    
# @receiver(post_save,sender=Cart)
# def update_cart_total(sender,instance,created,**kwargs):
#     if not created:
#         cart = instance
#         user = cart.created_by.id
#         cart = Cart.objects.filter(created_by=user)
#         cart = cart.annotate(total_price=Sum('order_items__name__price')).get()
#         print(cart.total_price)
        
   