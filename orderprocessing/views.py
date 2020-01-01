from django.shortcuts import render
from cart.models import *
from products.models import Product
from django.http import HttpResponse
from .models import *

# Create your views here.
def getaddress(request):
    promocode = request.session.get('promocode',None)
    total = 0
    cart_dict_list =[]
    cartobj = Cart.objects.filter(user=request.user).select_related('color').values()
    for i in cartobj:
        cart_dict_list.append(i)
    for i in cart_dict_list:
        color_obj = Color_variation.objects.select_related("product").get(id=i["color_id"])
        i["name"] = color_obj.product.Product_Name
        i["color"] = color_obj.color
        i["price"] = i['Quantity']*color_obj.product.Current_Price
        total = total + i['Quantity']*color_obj.product.Current_Price
    return render(request,'checkout.html',{'cart_products':cart_dict_list,"total":total,'promocode':promocode})

def get_order(request):
    f_name = request.POST.get('fname')
    l_name = request.POST.get('lname')
    address = request.POST.get('address')
    city = request.POST.get('city')
    pin_code = request.POST.get('zip')
    phone = request.POST.get('phone')
    a_phone = request.POST.get('a_phone')
    e_mail = request.POST.get('e_mail')
    state = request.POST.get('state')
    save_flag = request.POST.get('save_addr')
    cartobj = Cart.objects.filter(user=request.user).select_related('color')
    if not a_phone:
        a_phone = 000

    checkout_obj = Checkout.objects.create(user=request.user,
    first_name=f_name,
    last_name=l_name,
    address = address,
    city= city,
    state = state,
    number = phone,
    alt_number = phone,
    pincode = pin_code,
    email = e_mail
    )
    
    for i in cartobj:
        sell_price = 0
        prodobj = Product.objects.get(id=i.color.product_id)
        if  prodobj.Offer_price:
            sell_price = prodobj.Offer_price
        else:
            sell_price = prodobj.Current_Price
        price = prodobj.Current_Price
        Ordered_products.objects.create(checkout=checkout_obj,product=i.color.product,color=i.color.color,quantity=i.Quantity,Image=i.color.Image_one,sell_price=sell_price,price=price)
    cartobj.delete()
    return render(request,'thankyou.html')