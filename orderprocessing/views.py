from django.shortcuts import render
from cart.models import *
from products.models import Product
from django.http import HttpResponse
from .models import *
# Importing for pdf generation -----------------#
from django.template.loader import get_template #
from .utils import render_to_pdf                #
# ----------------------------------------------#

# Create your views here.
def getaddress(request):

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
    promocode = request.session.get('promocode',None)
    cashback = None
    new_total = None
    if promocode:
        promobj = Promocodes.objects.get(code=promocode)
        if promobj.cashback_type == '1':  # Calculaton on basis of percentage
            cashback = total*(promobj.cashback/100)
            if cashback > promobj.max_cashback:
                cashback = promobj.max_cashback
        else:                           # Calculaton on basis of price
                cashback = promobj.cashback
        new_total = total - cashback
    return render(request,'checkout.html',{'cart_products':cart_dict_list,"total":total,'promocode':promocode,
    "cashback":cashback,"new_total":new_total})

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
    promocode = request.session.get('promocode',None)
    if promocode:
        promocode = Promocodes.objects.get(code=promocode)
        del request.session['promocode']
    checkout_obj = Checkout.objects.create(user=request.user,
    first_name=f_name,
    last_name=l_name,
    address = address,
    city= city,
    state = state,
    number = phone,
    alt_number = phone,
    pincode = pin_code,
    email = e_mail,
    promocode=promocode
    )

    for i in cartobj:
        sell_price = 0
        prodobj = Product.objects.get(id=i.color.product_id)
        if  prodobj.Offer_price:
            sell_price = prodobj.Offer_price
        else:
            sell_price = prodobj.Current_Price
        price = prodobj.Price
        Ordered_products.objects.create(checkout=checkout_obj,product=i.color.product,
                                        color=i.color.color,quantity=i.Quantity,Image=i.color.Image_one,
                                        sell_price=sell_price,price=price,size=i.size)
    cartobj.delete()
    return render(request,'thankyou.html')

def order_history(request):
    checkout_list = Checkout.objects.filter(user=request.user).values_list('id',flat=True)
    order_obj = Ordered_products.objects.select_related('checkout').select_related('product').filter(checkout__in=checkout_list)
    return render(request,'order_history.html',{"products":order_obj})

def place_ret_request(request):
    url = request.get_full_path()
    print(url)
    temp = url.split("req")
    id = temp[1]
    return render(request,'get_return_feedback.htm' ,{"id":id})

def get_fb(request):
    cp_id = request.POST.get('c_id')
    fb = request.POST.get('fb')
    print(fb,cp_id)
    RerurnRequest.objects.create(user=request.user,product_id=cp_id,feedback=fb)
    Ordered_products.objects.filter(id=int(cp_id)).update(status=5)
    return HttpResponse("created")

def GeneratePDF(request):
    url = str(request.get_full_path())
    url = url.split("?")
    c_id = int(url[1])
    order_obj = Ordered_products.objects.select_related('checkout').select_related('product').get(id=c_id)
    template = get_template('invoice.html')
    i = {
        "Ch_id":c_id,
        "address": order_obj.checkout.address,
        "city":order_obj.checkout.city,
        "state":order_obj.checkout.state,
        "c_name":order_obj.checkout.first_name,
        "email":order_obj.checkout.email,
        "d_recieved":(order_obj.price - order_obj.sell_price)*order_obj.quantity,
        "pin":order_obj.checkout.pincode,
        "pno":order_obj.checkout.number,
        "p_name":order_obj.product,
        "qty":order_obj.quantity,
        "u_price":order_obj.price,
        "total":order_obj.price * order_obj.quantity,
        "tax":(0.18) * order_obj.quantity,
        "discount": (order_obj.price - order_obj.sell_price),
        "date" : order_obj.checkout.date
    }
    print("generating..............")
    html = template.render(i)
    print("generating.........KKKK.....")
    pdf = render_to_pdf('invoice.html',i)
    print("generating.....OOOOOOOO.........")
    return HttpResponse(pdf,content_type='application/pdf')