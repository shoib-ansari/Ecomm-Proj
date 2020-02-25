from django.shortcuts import render 
from django.http import HttpResponse ,JsonResponse , HttpResponseRedirect
from django.core import serializers
from .models import *
from useraccounts.views import getnavitems , add_to_suggestions
from cart.models import *
from django.db.models import Q
from orderprocessing.models import Checkout , Ordered_products
from useraccounts.models import SuggestTags


# Create your views here.
def get_searched_products(request,s_l):
    sl= s_l.split(",")
    return Product.objects.filter(id__in=sl)
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

def filter_brands(request,prodobj,brands):
    id_list = []
    for i in prodobj:
        if i.brand in brands:
            id_list.append(i.id)
    prodobj = Product.objects.filter(id__in=id_list)
    return prodobj

def size_filter(request,prodobj,size_list):
    color_ids = []
    prod_ids = []
    size_obj = Size_variation.objects.filter(size__in=size_list)
    for i in size_obj:
        if not i.color_id in color_ids:
            color_ids.append(i.color_id)
    color_obj = Color_variation.objects.filter(id__in=color_ids)
    for i in color_obj:
        if not i.product_id in prod_ids:
            prod_ids.append(i.product_id)
    return prodobj.filter(id__in=prod_ids)
    
def get_wishlist(request):
    if request.user.is_authenticated:
        return Wishlist.objects.filter(user=request.user)
    else:
        return Wishlist.objects.none()

def get_products_of_subcat(request,sub_cat):
    sub_cat_obj = SubCategory.objects.get(id=sub_cat)
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
    cat_id = request.GET.get('cat_id')
    cat_obj = list(SubCategory.objects.filter(main_category_id=cat_id).values_list('id',flat=True))
    return JsonResponse(cat_obj,safe=False)

def showproducts(request):
    brand_list = []
    nav_product_dict = getnavitems(request)
    url = request.get_full_path()
    temp = url.split("in")
    sub_cat = temp[1]
    gotdata = ''
    try:
        gotdata = temp[2]
    except IndexError:
        gotdata = None
    if (sub_cat.find('M') != -1): 
        # If clicked on main category
        main_id = sub_cat.split("of")
        main_id = int(main_id[1])
        categories = SubCategory.objects.filter(main_category_id=main_id)
        prodobj = Product.objects.filter(Main_category_id=main_id)
        for i in prodobj:
            if i.brand not in brand_list and not i.brand is None:
                brand_list.append(i.brand)
        color_list = []
        id_list = []
        size_list = []
        color_id_list = []
        for i in prodobj:
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
        main_cat = MainCategory.objects.get(id=main_id)
        sub_cat_obj = SubCategory.objects.filter(main_category_id=main_id)
        return render(request,'shop.html',{"products":prodobj,"nav_products":nav_product_dict,"categories":categories,
        'colors':color_list,'sizes':size_list,"wishlist":wishlist,"brands":brand_list,"main_cat":main_cat})
        return HttpResponse(prodobj)
    else:
        # If clicked on SubCategories
        sub_cat_obj = SubCategory.objects.get(id=int(sub_cat))
        final_cat_set = FinalCategory.objects.filter(sub_category=sub_cat_obj)
        categories = FinalCategory.objects.filter(sub_category=sub_cat_obj.id)
        if gotdata:
            product_set = Product.objects.filter(Final_category_id=int(gotdata))
        else:
            product_set = Product.objects.filter(sub_category=sub_cat_obj)
        for i in product_set:
            if i.brand not in brand_list and not i.brand is None:
                brand_list.append(i.brand)
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
        main_cat = MainCategory.objects.all().distinct()
        return render(request,'shop.html',{"products":product_set,"nav_products":nav_product_dict,"categories":categories,
        'colors':color_list,'sizes':size_list,"sub_cat":sub_cat_obj.name,"wishlist":wishlist,"brands":brand_list,
        "sub_id":sub_cat_obj.id})

def show_detailed_product(request):
    nav_product_dict = getnavitems(request)
    url = request.get_full_path()
    temp = url.split("?")
    id = int(temp[1])
    prodobj = Product.objects.select_related('Final_category').select_related('sub_category').get(id=id)
    final_cat = prodobj.Final_category
    sub_cat = prodobj.sub_category
    related_products = Product.objects.filter(Q(Final_category=final_cat) & Q(sub_category=sub_cat))
    color_id =[]
    prod_color_set = Color_variation.objects.filter(product=prodobj)
    prod_size_dict = {}
    for i in prod_color_set:
        templist = []
        temp_set = Size_variation.objects.filter(color=i.id)
        for j in  temp_set:
            templist.append(j.size)
            prod_size_dict[i.id] = templist
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    review_obj = Reviews.objects.filter(product=prodobj).select_related('user')
    return render(request,'shop-single.html',{"product":prodobj,"nav_products":nav_product_dict,
    "color_variation":prod_color_set,"sizes":prod_size_dict,"cart_count":cart_count,
    "related_products":related_products,"reviews":review_obj})

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
    brands = request.GET.getlist('brand[]')
    main_cat = request.GET.get('main_cat')
    prodobj = Product.objects.none()
    if main_cat:
        prodobj=Product.objects.filter(Main_category=main_cat)
    elif final_cat:
        prodobj = Product.objects.filter(Final_category_id=final_cat)
    else:
        prodobj = get_products_of_subcat(request,products)
    if brands:
        prodobj = filter_brands(request,prodobj,brands)
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
    brands = request.GET.getlist('brand[]')
    if sizes:
        prodobj = size_filter(request,prodobj,sizes)
    prodobj = prodobj.filter(Final_category=int(final_cat_id))
    if colors:
        prodobj = color_filter(request,prodobj,colors)
    if brands:
        prodobj = filter_brands(request,prodobj,brands)
    if sort_criteria:
        prodobj = sort_products(request,prodobj,sort_criteria)
    wishobj = get_wishlist(request)
    data = [serializers.serialize('json', prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)

def get_products_of_group(request,group_id):
    product_list = Product_Group.objects.filter(group_id=group_id).values_list('product_id',flat=True)
    return Product.objects.filter(id__in=product_list)

def filter(request):
    wishobj = get_wishlist(request)
    sort_criteria = request.GET.get('sort_criteria')    
    final_cat = request.GET.get('final_cat')
    sizes = request.GET.getlist('size[]')
    products = request.GET.get('products')
    colors = request.GET.getlist('colors[]')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brands = request.GET.getlist('brand[]')
    main_cat = request.GET.get('main_cat')
    group_id = request.GET.get('group')
    s_l = request.GET.get('s_l')
    prodobj = Product.objects.none()
    if main_cat:
        prodobj=Product.objects.filter(Main_category=main_cat)
    elif final_cat:
        prodobj = Product.objects.filter(Final_category_id=final_cat)
    elif products:
        prodobj = get_products_of_subcat(request,products)
    elif group_id:
        prodobj = get_products_of_group(request,group_id)
    elif s_l:
        prodobj = get_searched_products(request,s_l)
    prodobj = price_filter(request,prodobj,min_price,max_price)
    if brands:
        prodobj = filter_brands(request,prodobj,brands)
    if sizes:
        prodobj = size_filter(request,prodobj,sizes)
    if colors:
        prodobj = color_filter(request,prodobj,colors)
    if sort_criteria:
        prodobj = sort_products(request,prodobj,sort_criteria)
    data = [serializers.serialize('json',prodobj),serializers.serialize('json', wishobj)]
    return JsonResponse(data, safe=False)

def search(request):
    query = request.GET.get('query')
    tags = list(Tags.objects.filter(name__icontains=query).values_list('name',flat=True)[:10])
    return JsonResponse(tags,safe=False)

def rate(request):
    prod_id = int(request.GET.get('prod_id'))
    curr_rating = int(request.GET.get('rate'))
    check_obj_list = Checkout.objects.filter(user=request.user).values_list('id',flat=True)
    ordered_ids = Ordered_products.objects.filter(id__in=check_obj_list).values_list('product_id',flat=True)
    if prod_id in list(ordered_ids):
        prodobj = Product.objects.get(id=prod_id)
        rating = prodobj.rating
        newrating = (rating*prodobj.total_ratings + curr_rating)/(prodobj.total_ratings + 1)
        prodobj.total_ratings = prodobj.total_ratings + 1
        prodobj.rating = newrating
        prodobj.save()
        review_obj, created = Reviews.objects.update_or_create(user=request.user,product=prodobj,defaults={'rating': curr_rating},)
        return_string = str(rating)+"^"
        return HttpResponse("permission granted")
    return HttpResponse("Denied^")

def review(request):
    ret_string = ''
    review = request.GET.get('review')
    p_id = int(request.GET.get('prod_id'))
    review_obj, created = Reviews.objects.update_or_create(user=request.user,product=Product.objects.get(id=p_id),defaults={'review': review})
    name = request.user.first_name
    if not name:
        name = request.user.username
    if created:
        ret_string = ret_string + '1~'+str(review_obj.id)+'~' +name +'~'+str(review_obj.rating)+'~'+str(review_obj.review)
    else:
        ret_string = ret_string + '0~'+str(review_obj.id)+'~'+name +'~'+str(review_obj.rating)+'~'+str(review_obj.review)
    return HttpResponse(ret_string)
    
        
    print(review_obj.rating)

def show_results(request):
    nav_product_dict = getnavitems(request)
    query = request.GET.get('query')
    tags = Tags.objects.filter(name__icontains=query)
    prod_list = []
    for i in tags:
        products = i.products.all()
        if products:
            for i in products:
                if i not in prod_list:
                    prod_list.append(i.id)
    product_set = Product.objects.filter(id__in=prod_list)
    brand_list = product_set.values_list('brand',flat=True).distinct().exclude(brand__isnull=True)
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
    main_cat = MainCategory.objects.all().distinct()
    prods = ''
    for i,j in enumerate(prod_list):
        if i ==0:
            prods = prods+str(j)
        else:
            prods= prods +","+str(j)
    return render(request,'shop.html',{"products":product_set,"nav_products":nav_product_dict,
    'colors':color_list,'sizes':size_list,"wishlist":wishlist,"brands":brand_list,"search_list":prods})

def get_cat_data(request):
    url = request.get_full_path()
    url = url.split("?")
    id = int(url[1])
    prodobj = Product.objects.select_related('sub_category').select_related('Final_category').get(id=id)
    sub_cat = "~"+prodobj.sub_category.name+"~"
    final_cat = "~"+prodobj.Final_category.name+"~"
    data_list = [sub_cat,final_cat]
    print("----------------------------",data_list)
    return JsonResponse(data_list,safe=False)

def get_images(request):
    images = request.FILES.getlist('reviewimages')
    review = request.POST.get('review')
    p_id = request.POST.get('p_id')
    prodobj = Product.objects.get(id=p_id)
    try:
        reviewobj = Reviews.objects.get(Q(product_id=prodobj.id) & Q(user=request.user))
        reviewobj.review = review
        reviewobj.save()
    except Reviews.DoesNotExist:
        reviewobj = Reviews.objects.create(product_id=prodobj.id,user=request.user,Review = review)
    for i in images:
        fs = FileSystemStorage(location='media/reviewpics')
        fs.save(i.name, i)
        reviewimageobj = Reviewimages.objects.create(image=i.name,review_id=reviewobj.id,product_id=prodobj.id,user_id=request.user.id)
    url = str(request.META.get('HTTP_REFERER'))+'#rt_rv'
    print("---------------------------------------",request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(url)

def showallproducts(request):
    url = request.get_full_path()
    main_id = url.split("in")[1]
    prodobj = Product.objects.filter(Main_category_id=main_id).select_related('sub_category').select_related('final_cat_set')
    
    final_cat_set = FinalCategory.objects.filter(sub_category=sub_cat_obj)
    categories = FinalCategory.objects.filter(sub_category=sub_cat_obj.id)
    for i in product_set:
        if i.brand not in brand_list and not i.brand is None:
            brand_list.append(i.brand)
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
    main_cat = MainCategory.objects.all().distinct()
    return render(request,'shop.html',{"products":product_set,"nav_products":nav_product_dict,"categories":categories,
    'colors':color_list,'sizes':size_list,"sub_cat":sub_cat_obj.name,"wishlist":wishlist,"brands":brand_list,"main_cat":main_cat})

def get_tag_data(request):
    url = request.get_full_path()
    temp = url.split('tag_data/')
    query = temp[1]
    query = query.replace("%20", " ")
    tags = list(Tags.objects.filter(name__icontains=query).values())
    return JsonResponse(tags,safe=False)

def check_tag_data(request):
    url = request.get_full_path()
    return_list = []
    temp = url.split('tag_data/')
    query = temp[1]
    query = query.replace("%20", " ")
    query = query.split(",")
    tagsobj_list = []
    for i in query:
        if len(i) > 0:
            obj , created = Tags.objects.get_or_create(name=i)
            tagsobj_list.append(obj)
    
    for i in tagsobj_list:
        return_dict = {}
        return_dict['id'] = i.id
        return_dict['name'] = i.name
        return_list.append(return_dict)
    return JsonResponse(return_list,safe=False)

def get_tags(request):
    url = request.get_full_path()
    url = url.split("/")
    p_id = int(url[9])
    prodobj = Product.objects.get(id=p_id)
    tags = prodobj.tags.all().values()
    tag_list = []
    for i in tags:
        tag_list.append(i)
    return JsonResponse(tag_list,safe=False)

def get_self_cat_prod(request):
    nav_product_dict = getnavitems(request)
    url = request.get_full_path()
    url = url.split('in')
    grp_id = url[1]
    products = Product_Group.objects.filter(group_id=grp_id).select_related('product')
    product_set = Product.objects.none()
    product_list = []
    for i in products:
        product_list.append(i.product.id)
    product_set = Product.objects.filter(id__in=product_list)
    brand_list = product_set.values_list('brand',flat=True).distinct().exclude(brand__isnull=True)
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
    main_cat = MainCategory.objects.all().distinct()
    return render(request,'shop.html',{"products":product_set,"nav_products":nav_product_dict,
    'colors':color_list,'sizes':size_list,"wishlist":wishlist,"brands":brand_list,"group":grp_id})