from django.urls import path,include , re_path
from . import views

urlpatterns = [
    path('add_to_wishlist',views.add_to_wishlist,name="add product to wishlist"),
    path('add_to_cart',views.add_to_cart,name="add product to cart"),
]