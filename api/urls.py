from django.urls import path,include
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static
from .views import ProductsView,ProductDetailsView,ProductFilterView,ProductDeleteView,ProductCreateView,productUpdateView
from .views import CategoryView,CategoryDeleteView,CategoryCreateView,CategoryUpdateView,CategoryDetailsView
from .views import BrandView,BrandDeleteView,BrandCreateView,BrandUpdateView,BrandDetailsView
from .views import CartView,AddItemView,ItemDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  #auth endpoint
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('accounts/', include('rest_registration.api.urls')),
  #product endpoints
  path('products/',ProductsView.as_view()),
  path('product_create/',ProductCreateView.as_view()),
  path('product_details/<int:id>/',ProductDetailsView.as_view()),
  path('product_update/<int:id>/',productUpdateView.as_view()),
  path('product_delete/<int:id>/',ProductDeleteView.as_view()),
  path('productfilter/<str:category>/<str:num_of_products>/',ProductFilterView.as_view()),
  #category endpoints
  path('category/',CategoryView.as_view()),
  path('category_create/',CategoryCreateView.as_view()),
  path('category_details/<int:id>/',CategoryDetailsView.as_view()),
  path('category_update/<int:id>/',CategoryUpdateView.as_view()),
  path('category_delete/<int:id>/',CategoryDeleteView.as_view()),
  #Brand endpoints
  path('brand/',BrandView.as_view()),
  path('brand_create/',BrandCreateView.as_view()),
  path('brand_details/<int:id>/',BrandDetailsView.as_view()),
  path('brand_update/<int:id>/',BrandUpdateView.as_view()),
  path('brand_delete/<int:id>/',BrandDeleteView.as_view()),
  #item endpoints
  path('cart/<int:id>/',CartView.as_view()),
  path('add_item/',AddItemView.as_view()),
  path('item_delete/<int:id>/',ItemDeleteView.as_view()),

]

