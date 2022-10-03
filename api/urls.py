from django.urls import path,include
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static
from .views import ProductsView,ProductDetailsView,ProductFilterView,ProductDeleteView,ProductCreateView,productUpdateView,ProductAddDiscount
from .views import CategoryView,CategoryDeleteView,CategoryCreateView,CategoryUpdateView,CategoryDetailsView
from .views import BrandView,BrandDeleteView,BrandCreateView,BrandUpdateView,BrandDetailsView
from .views import CartView,AddItemView,ItemDeleteView
from .views import WishListView,AddToWishListView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="ecommerce API",
        default_version='v1'
    ),
    public=True,
)



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
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
  path('productfilter/<str:category>/',ProductFilterView.as_view()),
  path('add_discount/<int:id>/',ProductAddDiscount.as_view()),
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
  path('cart/',CartView.as_view()),
  path('add_item/',AddItemView.as_view()),
  path('item_delete/<int:id>/',ItemDeleteView.as_view()),
  #wish list endpoints
  path('wish_list/',WishListView.as_view()),
  path('add_to_wishlist/',AddToWishListView.as_view())

]

