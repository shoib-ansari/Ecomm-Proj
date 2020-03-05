from . import views
from django.urls import path , re_path


urlpatterns = [
    path('',views.getaddress,name="Get address"),
    path('get_order',views.get_order,name="Get order Details"),
    path('get_fb',views.get_fb,name="Get feedback for return"),
    re_path(r'^return_req',views.place_ret_request,name="Place a return request"),
    re_path(r'^get_invoice',views.GeneratePDF,name="Generate pdf of invoice"),
    path('order_history',views.order_history,name="Get order history"),
    path('charge',views.charge,name="charge Payment"),
]