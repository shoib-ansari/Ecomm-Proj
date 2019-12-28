from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.core import serializers
from .models import *
from products.models import Color_variation
# from django.db.models import Count , Q

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
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    total = 0
    prod_list = []
    cart_obj = Cart.objects.filter(user=request.user).values()
    for i in cart_obj:
        prod_list.append(i)
    for i in prod_list:
        color_obj = Color_variation.objects.select_related("product").get(id=i["color_id"])
        i["max_price"] = color_obj.product.Price
        i["price"] = color_obj.product.Current_Price
        i["image"] = color_obj.Image_one.url
        i["color"] = color_obj.color
        i["name"] = color_obj.product.Product_Name
        total = total + i['Quantity']*i["price"]
    return render(request,'cart.html',{'cart_products':prod_list,"total":total,"cart_count":cart_count})

def update_cart(request):
    cart_count = Cart.objects.filter(user=request.user).values('color').distinct().count()
    return_string = ''
    flag = request.GET.get('data')
    total = 0
    prod_ids = []
    obj_id = request.GET.get('id')
    flag = request.GET.get('data')
    cart_obj = Cart.objects.get(id=obj_id)
    color_obj = Color_variation.objects.select_related('product').get(id=cart_obj.color.id)
    # If product is last of its kind
    if  cart_obj.Quantity == 1 and flag == 'down':
        cart_count = cart_count-1
        return_string = str(cart_obj.id)+"?"+str(color_obj.product.Current_Price)+"?N"+"?"+str(cart_count)
        cart_obj.delete()
    # If product is not last of its kind
    else:
        if flag == 'up':
            cart_obj.Quantity = cart_obj.Quantity + 1
            cart_obj.save()
        elif flag == 'down':
            cart_obj.Quantity = cart_obj.Quantity - 1
            cart_obj.save()
        return_string = str(cart_obj.id)+"?"+str(color_obj.product.Current_Price)+"?Y"+"?"+str(cart_count)
    return HttpResponse(return_string)