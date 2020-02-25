from .import views
from django.urls import path , re_path

urlpatterns = [
    path('apply_coupen',views.apply_coupen,name="apply coupen"),
    re_path(r'^offer_products_in',views.show_offerProds,name="Show offered Products"),
    path('rmv_coupon',views.remove_coupon,name="remove coupon")
]