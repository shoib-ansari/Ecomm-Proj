from django.contrib import admin
from .models import *
# Register your models here.


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','number','city','state','Mark_as_seen','date']
    list_filter = ["city","state","first_name"]
    search_fields = ["first_name","Keywords"]



class RerurnRequestAdmin(admin.ModelAdmin):
    list_display = ['user','product','feedback','seen_status','approved_for_return','return_status']
    list_filter = ["user","seen_status"]
    # search_fields = ["first_name","Keywords"]

class Ordered_productsAdmin(admin.ModelAdmin):
    list_display = ['product','color','size','sell_price','checkout','quantity']
    # list_filter = ["user","seen_status"]


admin.site.register(Checkout,CheckoutAdmin)
admin.site.register(Ordered_products,Ordered_productsAdmin)
admin.site.register(RerurnRequest,RerurnRequestAdmin)

