from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.core import serializers
from .models import *
from products.models import *
from offers.models import Promocodes
from orderprocessing.models import Checkout
from django.db.models import Sum
from django.db.models import Count , Q
from useraccounts.views import getnavitems , add_to_suggestions

# Create your views here.

def add_to_wishlist(request):
    prod_id = request.GET.get('product_id')
    try:
        wishobj = Wishlist.objects.get(user=request.user,product_id=prod_id)
        wishobj.delete()
    except Wishlist.DoesNotExist:
        Wishlist.objects.create(user=request.user,product_id=prod_id)
    ret_string = "wish_obj_"+str(prod_id)
    return HttpResponse(ret_string)


def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    color = request.GET.get('Color')
    size = request.GET.get('size')
    quantity = request.GET.get('quantity')
    try:
        cartobj = Cart.objects.get(user=request.user,size=size,color_id=color)
        cartobj.Quantity = cartobj.Quantity + 1
        cartobj.save()
    except Cart.DoesNotExist:
        Cart.objects.create(user=request.user,Quantity=quantity,size=size,color_id=color)
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    return HttpResponse(cart_count)

def show_cart(request):
    nav_product_dict = getnavitems(request)
    promobj = Checkout.objects.filter(Q(promocode__isnull=True) and Q(user=request.user)).values('promocode').distinct()
    appliedcode = []
    for i in promobj:
        appliedcode.append(i['promocode'])
    promobj = Promocodes.objects.all()
    prev_codes = []
    for i in appliedcode:
        counter = Checkout.objects.filter(Q(promocode__isnull=False) & Q(user=request.user)
            and Q(promocode=i)).count()
        prev_codes.append((i,counter))
    invalid_codes = []
    for i in prev_codes:
        if i[0] is not None:
            code_counter = Checkout.objects.filter(Q(promocode=i[0]) & Q(user=request.user)).count()
            print(code_counter)
            if code_counter >= Promocodes.objects.get(id=i[0]).applicabe_for_transactions:
                invalid_codes.append(i[0])
    available_codes = Promocodes.objects.all().exclude(id__in=invalid_codes) 
    promo_obj = available_codes
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    total = 0
    prod_dict_list = []
    cart_obj = Cart.objects.filter(user=request.user).values()
    for i in cart_obj:
        prod_dict_list.append(i)
    for i in prod_dict_list:
        color_obj = Color_variation.objects.select_related("product").get(id=i["color_id"])
        i["max_price"] = color_obj.product.Price
        i["price"] = color_obj.product.Current_Price
        i["image"] = color_obj.Image_one.url
        i["color"] = color_obj.color
        i["name"] = color_obj.product.Product_Name
        total = total + i['Quantity']*i["price"]
    # Checking for promocodes ---------
    cart_total =total
    cashback = 0
    promobj = Promocodes.objects.none()
    promocode = request.session.get('promocode',False)
    promocode = request.session.get('promocode',False)
    if promocode:
        promobj = Promocodes.objects.get(code=promocode)
        if cart_total >= promobj.min_transaction:
            if promobj.cashback_type == '1':  # Calculaton on basis of percentage
                value = promobj.cashback
                cashback= int(cart_total*(value/100))
                if cashback >= promobj.max_cashback:
                    print("zada hai...")
                    cashback = promobj.max_cashback
            else:               #Calculation on the basis of price
                value = promobj.cashback
                cashback= cart_total - value
                if cashback >= promobj.max_cashback:
                    cashback = promobj.max_cashback
            cart_total = total - cashback
    # if there is no promocodes
    if cart_total == total:
        cart_total = None
        cashback = None
    main_cat_nav = MainCategory.objects.all().distinct()
    print(main_cat_nav)
    return render(request,'cart.html',{'cart_products':prod_dict_list,"total":total,
    "cart_count":cart_count,"promocodes":promo_obj,"promocode":promocode,
    "total_after_cb":cart_total,"cashback":cashback,"nav_products":nav_product_dict,"main_cat_nav":main_cat_nav})

def update_cart(request):
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    return_string = ''
    # flag = request.GET.get('data')
    total = 0
    prod_ids = []
    obj_id = request.GET.get('id')
    flag = request.GET.get('data')
    cart_obj = Cart.objects.get(id=obj_id)
    color_obj = Color_variation.objects.select_related('product').get(id=cart_obj.color.id)

    # If product is last of its kind || sending '?N' if product has to be is removed in return_string
    if  cart_obj.Quantity == 1 and flag == 'down':
        cart_count = cart_count-1
        return_string = str(cart_obj.id)+"?"+str(color_obj.product.Current_Price)+"?N"+"?"+str(cart_count)
        cart_obj.delete()
    # If product is not last of its kind || sending '?Y' if product  in return_string
    else:
        if flag == 'up':
            cart_obj.Quantity = cart_obj.Quantity + 1
            cart_obj.save()
        elif flag == 'down':
            cart_obj.Quantity = cart_obj.Quantity - 1
            cart_obj.save()
        return_string = str(cart_obj.id)+"?"+str(color_obj.product.Current_Price)+"?Y"+"?"+str(cart_count)
    # Getting carttotal
    cart_total = 0
    cartobj = Cart.objects.filter(user=request.user).select_related('color')
    for i in cartobj:
        offer_price = Product.objects.get(id=i.color.product_id).Offer_price
        curr_price = Product.objects.get(id=i.color.product_id).Current_Price
        if offer_price == '':
            cart_total = cart_total + offer_price*(i.Quantity)
        else:
            cart_total = cart_total + curr_price*(i.Quantity)

    # Checking for promocodes --------
    cashback = 0
    code = request.session.get('promocode',None)
    if code:
        promobj = Promocodes.objects.get(code=code)
        # If promocode becomes Invalid
        if cart_total < promobj.min_transaction:
            return_string = return_string+"?remove"
            del request.session['promocode']
        # If promocode is valid
        else:
            if promobj.cashback_type == '1':  # Calculaton on basis of percentage
                cashback = cart_total*(promobj.cashback/100)
                if cashback > promobj.max_cashback:
                    cashback = promobj.max_cashback
            else:                           # Calculaton on basis of price
                cashback = promobj.cashback
            new_total = cart_total - cashback
            return_string = return_string+"?pass^"+str(new_total)+"^"+str(cashback)
    return HttpResponse(return_string)

def remove_prod_from_cart(request):
    cart_prod_id = request.GET.get('cart_prod_id')
    Cart.objects.get(id=cart_prod_id).delete()
    return HttpResponse("Deleted product successfully")
