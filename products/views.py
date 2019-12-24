from django.shortcuts import render 
from django.http import HttpResponse ,JsonResponse
from django.core import serializers
from .models import *
from useraccounts.views import getnavitems
from cart.models import *

# Create your views here.

# def sort_inner(request,)

def getsubcats(request):
    url = str(request.path)
    temp = url.split("/")
    selected_category = int(temp[3])
    sub_category = SubCategory.objects.filter(main_category=selected_category)
    subcatlist = []

    if sub_category:
        for i in sub_category:
            if len(subcatlist) == 0:
                subcatlist.append(i.id)
                subcatlist.append("^")
                subcatlist.append(i)
            else:
                subcatlist.append("%")
                subcatlist.append(i.id)
                subcatlist.append("^")
                subcatlist.append(i)
    return HttpResponse(subcatlist)


def getfinalcategories(request):

    url = str(request.path)
    temp = url.split("/")
    selected_category = int(temp[3])
    final_category = FinalCategory.objects.filter(sub_category=selected_category)

    finalcatlist = []
    if final_category:
        for i in final_category:
            if len(finalcatlist) == 0:
                finalcatlist.append(i.id)
                finalcatlist.append("^")
                finalcatlist.append(i)
            else:
                finalcatlist.append("%")
                finalcatlist.append(i.id)
                finalcatlist.append("^")
                finalcatlist.append(i)
    return HttpResponse(finalcatlist)

def getsubcat(request):

    subcat = request.GET.get("category")
    cat_id = MainCategory.objects.get(name=subcat)
    subcategories = SubCategory.objects.filter(main_category=cat_id)
    subcatlist = []
    if subcategories:
        for i in subcategories:
            if len(subcatlist) == 0:
                subcatlist.append(i.id)
                subcatlist.append("^")
                subcatlist.append(i)
            else:
                subcatlist.append("%")
                subcatlist.append(i.id)
                subcatlist.append("^")
                subcatlist.append(i)
    return HttpResponse(subcatlist)

def showproducts(request):
    nav_product_dict = getnavitems(request)
    url = request.get_full_path()
    temp = url.split("in")
    sub_cat = temp[1]
    sub_cat_obj = SubCategory.objects.get(name=sub_cat)
    final_cat_set = FinalCategory.objects.filter(sub_category=sub_cat_obj)
    categories = FinalCategory.objects.filter(sub_category=sub_cat_obj.id)
    product_set = Product.objects.filter(sub_category=sub_cat_obj)
    color_list = []
    id_list = []
    size_list = []
    color_id_list = []
    for i in product_set:
        id_list.append(i.id)
        colors = Color_variation.objects.filter(product=i)
        for i in colors:
            color_id_list.append(i.id)
            if i.color not in color_list:
                color_list.append(i.color)
    size_set = Size_variation.objects.filter(color__in=color_id_list)
    for i in size_set:
        size_list.append(i.size)

    wishlist = []
    if request.user.is_authenticated:
        wishobj = Wishlist.objects.filter(user=request.user)
        for i in wishobj:
            wishlist.append(i.product_id)

    return render(request,'shop.html',{"products":product_set,"nav_products":nav_product_dict,"categories":categories,'colors':color_list,'sizes':size_list,"sub_cat":sub_cat,"wishlist":wishlist})

def show_detailed_product(request):
    nav_product_dict = getnavitems(request)
    url = request.get_full_path()
    temp = url.split("?")
    id = int(temp[1])
    prodobj = Product.objects.get(id=id)
    color_id =[]
    prod_color_set = Color_variation.objects.filter(product=prodobj)
    prod_size_dict = {}
    for i in prod_color_set:
        templist = []
        temp_set = Size_variation.objects.filter(color=i.id)
        for j in  temp_set:
            templist.append(j.size)
            prod_size_dict[i.id] = templist
    return render(request,'shop-single.html',{"product":prodobj,"nav_products":nav_product_dict,"color_variation":prod_color_set,"sizes":prod_size_dict})


def sort(request):
    sort_criteria = request.GET.get('sort_criteria')
    products_ids = request.GET.getlist('products[]')
    prodobj = Product.objects.none()
    if sort_criteria == 'lth':
        prodobj = Product.objects.filter(id__in=products_ids).order_by('Current_Price')
    elif sort_criteria == 'htl':
        prodobj = Product.objects.filter(id__in=products_ids).order_by('-Current_Price')
    else:
        # Rating filter here
        pass
    wishobj = Wishlist.objects.filter(user=request.user)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)


def filter_final_cat(request):
    final_cat_id = request.GET.get('cat_id')
    prodobj = Product.objects.filter(Final_category=int(final_cat_id))
    wishobj = Wishlist.objects.filter(user=request.user)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)


def filter(request):
    sort_criteria = request.GET.get('sort_criteria')    
    cat = request.GET.get('cat')
    sizes = request.GET.getlist('size')
    print("---------------------------------------------------------------------")
    print("------------------------------------------------",sort_criteria)
    print("-------------------------------------------------------",cat)
    print("----------------------------------------------",sizes)