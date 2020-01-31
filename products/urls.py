from django.urls import path,include , re_path
from . import views

urlpatterns = [
    re_path(r'^getsubcategories',views.getsubcats,name="subcats"),
    re_path(r'^getfinalcategories',views.getfinalcategories,name="get final categories"),
    path('getsubcat',views.getsubcat,name="get sub categories"),
    re_path(r'^sub_productsin',views.showproducts,name="get final categories"),
    re_path(r'^All_prod_in',views.showallproducts,name="get final categories"),
    re_path(r'^get_cat_data',views.get_cat_data,name="get categories data"),
    re_path(r'^get_tag_data',views.get_tag_data,name="get tags data"),
    re_path(r'^check_tag_data',views.check_tag_data,name="check tags data"),
    re_path(r'^get_tags',views.get_tags,name="Get products tags"),
    re_path(r'^view_',views.show_detailed_product,name="Show product on single page"),
    re_path(r'self_categoriesin',views.get_self_cat_prod,name='Get products of categories'),
    path('sort',views.sort,name="Sort Products through Ajax"),
    path('filter_final_cat',views.filter_final_cat,name="filter final category through Ajax"),
    path('filter',views.filter,name='filter price, size and color'),
    path('rate',views.rate,name='Rate the product'),
    path('review',views.review,name='Give review for the product'),
    path('search',views.search,name='search products'),
    path('show_results',views.show_results,name='search products'),
    path('get_images',views.get_images,name='search products images from user'),
]