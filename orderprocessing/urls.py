from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.getaddress,name="Get address"),
    path('get_order',views.get_order,name="Get order Details")
]