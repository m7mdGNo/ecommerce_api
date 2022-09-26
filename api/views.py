from itertools import product
from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework import generics
from .models import Product,Category,Brand,Cart,Item
from .serilizers import ItemSerializer, ProdcutSerializer,CategorySerializer,BrandSerializer,CartSerializer
from rest_framework.response import Response



# handle product operations
class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer

class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class productUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class ProductDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer
    lookup_field = 'id'

class ProductFilterView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer

    def get_objects(self,category):
        try:
            return self.queryset.filter(category=category)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request,category,num_of_products):
        try:
            products = self.get_objects(category=Category.objects.get(name=category))[:int(num_of_products)]
            serializer = ProdcutSerializer(products,many=True)
            return Response(serializer.data)
        
        except:   
            products = self.get_objects(category=Category.objects.get(name=category))
            serializer = ProdcutSerializer(products,many=True)
            return Response(serializer.data)

# handle Category operations
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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
    lookup_field = 'id'

    def get(self,request,id,*args, **kwargs):
        user = request.user
        cart = Cart.objects.get(created_by=user)
        items = Item.objects.filter(user=user)
        total = 0
        for item in items:
            product = Product.objects.get(id=item.name.id)
            total += product.price*Item.objects.get(id=item.id).qty
            cart.order_items.add(item)
        cart.total = total
        cart.save()
        serializer = CartSerializer(Cart.objects.filter(id=id),many=True)
        return Response(serializer.data)

class AddItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
