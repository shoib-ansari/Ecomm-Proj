from .import views
from django.urls import path



urlpatterns = [
    path('apply_coupen',views.apply_coupen,name="apply coupen"),
    path('check_coupon',views.check_coupon,name="apply coupen")
]