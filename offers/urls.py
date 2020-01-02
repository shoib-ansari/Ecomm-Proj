from .import views
from django.urls import path



urlpatterns = [
    path('apply_coupen',views.apply_coupen,name="apply coupen"),
    path('rmv_coupon',views.remove_coupon,name="remove coupon")
]