from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework import generics
from .models import Product,Category,Brand,Cart,Item,wishlist,wishlist_items
from .serilizers import ProdcutSerializer,CategorySerializer,BrandSerializer,CartSerializer,CreateItemSerializer,DeleteItemSerializer,ProdcutAddDiscountSerializer,UpdateProdcutSerializer
from .serilizers import WishListSerializer,Add_item_to_wishlistSerializer
from rest_framework.response import Response
from django.db.models import Sum,Count
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import Is_admin_mixins


# handle product operations
class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class productUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProdcutSerializer
    lookup_field = 'id'

class ProductDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class ProductFilterView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(category=self.kwargs['category'])

class ProductAddDiscount(Is_admin_mixins,generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutAddDiscountSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        product = Product.objects.filter(id=self.kwargs['id']).get()
        product.price_after_discount = product.price-(product.price*(product.discount/100))
        product.save() 
        return response

# handle Category operations
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all().annotate(num_of_products=Count('product'))
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

# handle Brand operations
class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BrandCreateView(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailsView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'

class BrandUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'

class BrandDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'

#add to card operations
class CartView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


    def get_object(self):
        cart = Cart.objects.filter(created_by=self.request.user).annotate(total_price=Sum('order_items__name__price')).get()
        cart.total = cart.total_price
        return cart

class AddItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = CreateItemSerializer

class ItemDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = DeleteItemSerializer
    lookup_field = 'id'

#add to wishlist operations
class WishListView(generics.ListAPIView):
    queryset = wishlist.objects.all()
    serializer_class = WishListSerializer

class AddToWishListView(generics.ListCreateAPIView):
    queryset = wishlist_items.objects.all()
    serializer_class = Add_item_to_wishlistSerializer