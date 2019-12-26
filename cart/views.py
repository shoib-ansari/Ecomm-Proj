from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from.models import *

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
    color = request.GET.get('color')
    size = request.GET.get('size')
    quantity = request.GET.get('quantity')
    Cart.objects.create(user=request.user,Quantity=quantity,size=size,color=color,product_id=product_id)
    cart_count = Cart.objects.filter(user=request.user).values('product').distinct().count()
    print("-----------------------------------------------------",cart_count)
    return HttpResponse(cart_count)
