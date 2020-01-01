from django.shortcuts import render 
from django.http import HttpResponse ,JsonResponse
from django.core import serializers
from .models import *
from useraccounts.views import getnavitems
from cart.models import *
from django.db.models import Q


# Create your views here.

def price_filter(request,prodobj,min_price,max_price):
    return prodobj.filter(Q(Current_Price__gte=int(min_price)) & Q(Current_Price__lte=(max_price)))

def color_filter(request,prodobj,colors):
    prod_ids = []
    color_list = []
    for i in prodobj:
        prod_ids.append(i.id)
    color_obj = Color_variation.objects.filter(product_id__in=prod_ids)
    for i in color_obj:
        if i.color in colors:
            color_list.append(i.product_id)
    return Product.objects.filter(id__in=color_list)

def size_filter(request,prodobj,size_list):
    color_ids = []
    prod_ids = []
    size_obj = Size_variation.objects.filter(size__in=size_list)
    print("---------",size_obj)
    for i in size_obj:
        if not i.color_id in color_ids:
            color_ids.append(i.color_id)
    color_obj = Color_variation.objects.filter(id__in=color_ids)
    for i in color_obj:
        if not i.product_id in prod_ids:
            prod_ids.append(i.product_id)
    print("----------------------",color_obj)
    print("----------------------",prod_ids)
    return prodobj.filter(id__in=prod_ids)
    
def get_wishlist(request):
    if request.user.is_authenticated:
        return Wishlist.objects.filter(user=request.user)
    else:
        return Wishlist.objects.none()

def get_products_of_subcat(request,sub_cat):
    sub_cat_obj = SubCategory.objects.get(name=sub_cat)
    return Product.objects.filter(sub_category=sub_cat_obj)

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
        if not i.size in size_list:
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
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    return render(request,'shop-single.html',{"product":prodobj,"nav_products":nav_product_dict,"color_variation":prod_color_set,"sizes":prod_size_dict,"cart_count":cart_count})

def sort_products(request,prodobj,sort_criteria):
    if sort_criteria == 'lth':
        return prodobj.order_by('Current_Price')
    elif sort_criteria == 'htl':
        return prodobj.order_by('-Current_Price')
    else:
        # Rating filter here
        pass

def sort(request):
    sort_criteria = request.GET.get('sort_criteria')
    products = request.GET.get('products')
    sizes = request.GET.getlist('size[]')
    final_cat = request.GET.get('inner_sort')
    colors = request.GET.getlist('colors[]')
    prodobj = Product.objects.none()
    if final_cat:
        prodobj = Product.objects.filter(Final_category_id=final_cat)
    else:
        prodobj = get_products_of_subcat(request,products)
    if sizes:
        prodobj = size_filter(request,prodobj,sizes)
    if colors:
        prodobj = color_filter(request,prodobj,colors)
    prodobj = sort_products(request,prodobj,sort_criteria)
    # Get wishlist
    wishobj = get_wishlist(request)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)

def filter_final_cat(request):
    final_cat_id = request.GET.get('cat_id')
    sizes = request.GET.getlist('size[]')
    prodobj = Product.objects.all()
    colors = request.GET.getlist('colors[]')
    sort_criteria = request.GET.get('sort_criteria')    
    if sizes:
        prodobj = size_filter(request,prodobj,sizes)
    prodobj = prodobj.filter(Final_category=int(final_cat_id))
    if colors:
        prodobj = color_filter(request,prodobj,colors)
    if sort_criteria:
        prodobj = sort_products(request,prodobj,sort_criteria)
    # get wishlist
    wishobj = get_wishlist(request)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)

def filter(request):
    # get wishlist
    wishobj = get_wishlist(request)
    sort_criteria = request.GET.get('sort_criteria')    
    final_cat = request.GET.get('final_cat')
    sizes = request.GET.getlist('size[]')
    products = request.GET.get('products')
    colors = request.GET.getlist('colors[]')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if final_cat:
        prodobj = Product.objects.filter(Final_category_id=final_cat)
    else:
        prodobj = get_products_of_subcat(request,products)
    prodobj = price_filter(request,prodobj,min_price,max_price)
    if sizes:
        prodobj = size_filter(request,prodobj,sizes)
    if colors:
        prodobj = color_filter(request,prodobj,colors)
    if sort_criteria:
        prodobj = sort_products(request,prodobj,sort_criteria)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)

def search(request):
    query = request.GET.get('query')
    print("-----------------------------------------------------------------")
    print(query)
    querylist = query.split(" ")
    resultid = []
    for i in querylist:
        prodobj = Product.objects.filter(Product_Name__icontains=i)
        for j in prodobj:
            resultid.append(j.id)
    for i in querylist:
        prodobj = Product.objects.filter(Keywords__icontains=i)
        for j in prodobj:
            resultid.append(j.id)
    searchid = []
    for i in resultid:
        if i not in searchid:
            searchid.append(i)
    print("-----------------------------------||||------------------------------")
    print(searchid)
    prodobj = Product.objects.values('Product_Name').filter(id__in=searchid)
    # print(type(prodobj))
    # print("search kr lia..............................")
    # import json
    # prodobj = json.dumps(prodobj, sort_keys=True)
    # return JsonResponse(serializers.serialize('json',prodobj), safe=False)
    return HttpResponse(prodobj)
