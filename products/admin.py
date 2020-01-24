from django.contrib import admin
from .models import MainCategory , SubCategory , FinalCategory ,Product , Color_variation , Size_variation
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from offers.models import Offer
# Register your models here.

class SubCategoryInline(admin.TabularInline):

    model = SubCategory
    extra = 0

class FinalCategoryInline(admin.TabularInline):

    model = FinalCategory
    extra = 0

class Size_variationInline(NestedStackedInline):
    model = Size_variation
    extra = 0
    fk_name = 'color'


class Color_variationInline(NestedStackedInline):
    model = Color_variation
    extra = 1
    fk_name = 'product'
    inlines = [Size_variationInline]

class MainCategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline,FinalCategoryInline]
    class Media:
        js = ('/static/js/category.js','https://code.jquery.com/jquery-3.3.1.min.js')

class ProductAdmin(NestedModelAdmin):

    model = Product
    list_display = ['Product_Name','Total_stock','date']
    inlines = [Color_variationInline]
    list_filter = ["date","Main_category","sub_category"]
    search_fields = ["Product_Name","Keywords"]

    def save_model(self, request, obj, form, change):
        if change == True:
            if obj.offer_id is None:
                obj.Offer_price = 0
                # obj.disc_per = 100 - (obj.pdiscount/obj.pprice)*100
            else:
                # wishobj = Wishlist.objects.filter(product=obj)
                # for i in wishobj:
                #     notification_obj = Notifications.objects.create(
                #         user = User.objects.get(id=i.user_id),
                #         title = obj.offer.name,
                #         notification = "there is a new offer on the product that you have reviewed",
                #         link = "view?"+ str(i.product.id)
                #     )
                # prodobj = Product.objects.get(id=obj.id)
                offerobj = Offer.objects.get(id=obj.offer_id)
                obj.Offer_price = int(obj.Current_Price*((100-offerobj.discount)/100))
                obj.disc_per = offerobj.discount
                obj.offer_id = offerobj.id
        super().save_model(request, obj, form, change)
    
    def Remove_all_offers(self,request,queryset):
        for obj in queryset:
            if obj.offer_id is not None:
                obj.offerprice = 0
                obj.disc_per = 100 -(obj.pdiscount / obj.pprice) * 100
                obj.offer_id = None
                obj.save()

    class Media:
        css = {
        'all': ('/static/css/style.css',)
         }
        js = ('/static/js/chained_dropdown.js','https://code.jquery.com/jquery-3.3.1.min.js',)




admin.site.register(MainCategory,MainCategoryAdmin)
admin.site.register(Product,ProductAdmin)

