from django.urls import path,include , re_path
from . import views

urlpatterns = [
    re_path(r'^getsubcategories',views.getsubcats,name="subcats"),
    re_path(r'^getfinalcategories',views.getfinalcategories,name="get final categories"),
    path('getsubcat',views.getsubcat,name="get sub categories"),
    re_path(r'^sub_productsin',views.showproducts,name="get final categories"),
    re_path(r'^view_',views.show_detailed_product,name="Show product on single page"),
    path('sort',views.sort,name="Sort Products through Ajax"),
    path('filter_final_cat',views.filter_final_cat,name="filter final category through Ajax"),
    path('filter',views.filter,name='filter price, size and color'),
    path('search',views.search,name='search products')
]