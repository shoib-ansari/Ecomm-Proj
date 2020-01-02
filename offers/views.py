from django.shortcuts import render
from cart.models import Cart
from products.models import Product
from offers.models import Promocodes
from django.http import HttpResponse
# Create your views here.

def apply_coupen(request):
    code = request.GET.get('code')
    cart_total = 0
    cartobj = Cart.objects.filter(user=request.user).select_related('color')
    for i in cartobj:
        offer_price = Product.objects.get(id=i.color.product_id).Offer_price
        curr_price = Product.objects.get(id=i.color.product_id).Current_Price
        if offer_price == '':
            cart_total = cart_total + offer_price*(i.Quantity)
        else:
            cart_total = cart_total + curr_price*(i.Quantity)
    promobj = Promocodes.objects.get(code=code)
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
        return_data = code+","+str(cashback)+","+str(cart_total-cashback)
        request.session['promocode'] = code

    else:
        return_data = code+",invalid cart amount"

    # promocode = request.session.get('promocode',None)
    return HttpResponse(return_data)

def remove_coupon(request):
    cartobj = Cart.objects.filter(user=request.user).select_related('color')
    cart_total = 0
    for i in cartobj:
        offer_price = Product.objects.get(id=i.color.product_id).Offer_price
        curr_price = Product.objects.get(id=i.color.product_id).Current_Price
        if offer_price == '':
            cart_total = cart_total + offer_price*(i.Quantity)
        else:
            cart_total = cart_total + curr_price*(i.Quantity)
    del request.session['promocode']
    return HttpResponse(cart_total)