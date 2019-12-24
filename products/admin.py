from django.contrib import admin
from .models import MainCategory , SubCategory , FinalCategory ,Product , Color_variation , Size_variation
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

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

    class Media:
        js = ('/static/js/chained_dropdown.js','https://code.jquery.com/jquery-3.3.1.min.js',)




admin.site.register(MainCategory,MainCategoryAdmin)
admin.site.register(Product,ProductAdmin)

