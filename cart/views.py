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

    
