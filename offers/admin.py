from django.contrib import admin
from .models import *
from products.models import Product
# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print("object is...",obj)
        if change == True:
            print("there is a change")
            if obj.end_offer == True:
                prodobj = Product.objects.filter(offer=obj)
                print("--------------------",prodobj)
                for i in prodobj:
                    i.offer_id = None
                    i.Offer_price = 0
                    i.save()
                    print("saved................")
            # else:
            #     prodobj = Product.objects.filter(offer=obj)
            #     for i in prodobj:
            #         i.save()
        obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Offer,OfferAdmin)
admin.site.register(Promocodes)