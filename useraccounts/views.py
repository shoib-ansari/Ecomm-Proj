from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse , HttpResponse
from .models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from products.models import *
from cart.models import Cart
import json
from django.db.models import Q
from notifications.models import Notifications
from django.core.mail import send_mail
from EcommerceWebsite.settings import EMAIL_HOST_USER
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from offers.models import *
import random

# Create your views here.

def getnavitems(request):
    product_dict = {}
    main_cat = MainCategory.objects.all().distinct()
    for i in main_cat:
        product_dict[i.name] = ''
        temp_sub_dict = {}
        sub_cat = SubCategory.objects.filter(main_category=i)
        if sub_cat:
            for j in sub_cat:
                temp_final_list = []
                temp_final_list.append(j.id)
                final_cat = FinalCategory.objects.filter(sub_category=j)
                if final_cat:
                    for k in final_cat:
                        last_list = []
                        last_list.append(k.id)
                        last_list.append(k.name)
                        temp_final_list.append(last_list)
                temp_sub_dict[j.name] = temp_final_list
            product_dict[i.name] = temp_sub_dict
    return product_dict


def get_noti_status(request):
    if request.user.is_authenticated:
        notiobj = Notifications.objects.filter(user=request.user,seen_by_user=False)
        if notiobj:
            return True
        else:
            return False
    else:
        return False

def add_to_suggestions(request,query):
    string = ''
    import re
    if request.user.is_authenticated:
        sobj , flag = SuggestTags.objects.get_or_create(user=request.user)
        if not len(re.findall(query, sobj.tags)):
            sobj.tags = sobj.tags + ","+ str(query)

            if len(re.findall(",", sobj.tags)) > 6:
                temp_list = sobj.tags.split(",")
                temp_list.pop(0)
                for i in temp_list:
                    string = string +i + ","
                sobj.tags =string
            sobj.save()

# def get_suggested_products(request):
#     if request.user.is_authenticated:
#         try:
#             sobj = SuggestTags.objects.get(user=request.user)
#             if sobj.tags:
#                 querylist = sobj.tags.split(",")
#                 product_list = []
#                 exception_list = ['for','in',]
#                 querylist = list(set(querylist) - set(exception_list))
#                 for i in querylist:
#                     prodobj = Product.objects.filter(Q(Product_Name__icontains=i) & Q(Keywords__icontains=i)).values()
#                     # prodobj is a set of products
#                     for j in prodobj:
#                         product_list.append(j)
#                 # using frozenset to remove duplicates  
#                 product_list = {frozenset(item.items()) : item for item in product_list}.values()
#                 for i in querylist:
#                     for j in product_list:
#                         j['counter'] = 0
#                         j['counter'] = j['counter'] + j['Product_Name'].count(i) + j['Keywords'].count(i)
#                 prod_list = sorted(product_list, key = lambda i: i['counter']) 
#                 prod_list.reverse()
#                 return prod_list
#         except SuggestTags.DoesNotExist:
#             return None
#     else:
#         return None

def homepage(request):
    import itertools
    
    main_header = []
    product_dict = getnavitems(request)
    noti_flag = get_noti_status(request)
    # suggest_prods = get_suggested_products(request)
    main_car_1 = Offer.objects.filter(add_to_main_header=True)
    print(main_car_1.model.__name__)
    main_car_2 = MainCategory.objects.filter(add_to_main_header=True)
    main_car_3 = SubCategory.objects.filter(add_to_main_header=True)
    main_car_4 = FinalCategory.objects.filter(add_to_main_header=True)
    main_header = itertools.chain(main_car_1,main_car_2,main_car_3,main_car_4)


    sub_car_2 = MainCategory.objects.filter(add_to_sub_header=True)
    sub_car_3 = SubCategory.objects.filter(add_to_sub_header=True)
    sub_car_4 = FinalCategory.objects.filter(add_to_sub_header=True)
    sub_header = itertools.chain(main_car_1,main_car_2,main_car_3,main_car_4)


    featured_obj = FeaturedProducts.objects.all()

    home_categories = HomePageCategories.objects.all()

    group_id =[]
    group_obj = Product_Group.objects.all().values('group_id').distinct().order_by('-group_id')
    for i in group_obj:
        group_id.append(i['group_id'])
    print(group_id)

    groups = []
    for i in group_id:
        temp_list = []
        temp_list.append(Group_products.objects.get(id=i))
        temp_list.append(Product_Group.objects.filter(group_id=i).values())
        print(len(temp_list))
        groups.append(temp_list)



    offers = Offer.objects.all()
    suggest_prods = None
    main_cat = MainCategory.objects.all().distinct()
    return render(request, "index.html",{"products":product_dict,"notification":noti_flag,"suggestions":suggest_prods,
    "main_cat":main_cat,"offers":offers,"main_header":main_header,"sub_header":sub_header,"featured_prods":featured_obj,
    "categories":home_categories,"groups":groups})
    

def register(request):
    name = request.POST.get('namedata', False)
    email = request.POST.get('emaildata', False)
    password = request.POST.get('passworddata', False)
    contact_number = request.POST.get('contactdata', False)

    if User.objects.filter(username=name).exists():
        return JsonResponse("Username allready exists", safe=False)

    else:
        userobj = User.objects.create(username=name, email=email, contact=contact_number, password=password)
        userobj.set_password(password)
        userobj.save()
        auth.login(request, userobj)
        return JsonResponse("user has been registered scusssfully", safe=False)

def logout(request):
    auth.logout(request)
    return redirect("/")

def checklogin(request):
    
    username = request.POST.get("usernamedata", False)
    password = request.POST.get("passworddata", False)

    user = auth.authenticate(request, username=username, password=password)
    if user:
        auth.login(request, user)
        return JsonResponse("Login granted", safe=False)
    else:
        try:
            tempuser = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse("Username not availabe", safe=False)

        if tempuser:
            return JsonResponse("Incorrect Password", safe=False)

def update_user_profile_page(request):

    product_dict = getnavitems(request)
    return render(request, "editprofile.html",{"products":product_dict})

def update_profile(request):
    return_dict = {}
    username = request.POST.get('username')
    e_mail = request.POST.get('e_mail')
    number = request.POST.get('number')
    password = request.POST.get('password')
    new_pwd = request.POST.get('new_pwd')
    user = auth.authenticate(request, username=request.user.username, password=password)
    if user:
        return_dict['status'] = 'profile updated'
        return_dict['username'] = username
        return_dict['email'] = e_mail
        return_dict['contact'] = number
        user.username = username
        user.email = e_mail
        user.contact = number
       
        if not new_pwd == 'false':
            return_dict['status'] = 'pwd_updated'
            user.set_password(new_pwd)
        user.save()
        return HttpResponse(json.dumps(return_dict),content_type="application/json")
    else:
        return_dict['status'] = 'invalid password'
        return HttpResponse(json.dumps(return_dict),content_type="application/json")

def addr_page(request):
    return render(request,'manage_addr.htm')

def update_addr(request):
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    address = request.POST.get('address')
    city = request.POST.get('city')
    postal_code = request.POST.get('postal_code')
    state = request.POST.get('state')
    e_mail = request.POST.get('e_mail')
    contact = request.POST.get('contact')
    alt_phone = request.POST.get('alt_phone')
    print("I am taking control.................")
    user = request.user
    user.first_name = f_name
    user.last_name = l_name
    user.address = address
    user.city = city
    user.postal_add = postal_code
    user.state = state
    user.email = e_mail
    user.contact = contact
    user.alt_contact = alt_phone
    user.save()
    return HttpResponse('Updated')


def f_p_page(request):
        return render(request,'forgot_pwd.html')

def send_recovery_code(request):
    v_code = request.GET.get('v_code')
    if v_code:
        mail = request.GET.get('mail')
        userobj = User.objects.get(email=mail)
        try:
            verobj = V_code.objects.get(user=userobj,code=v_code)
        except V_code.DoesNotExist:
            return HttpResponse("invalid Code")
        if verobj:
            verobj.delete()
            auth.login(request,userobj)
            return HttpResponse("logged inn")

    string = ''
    ver_obj = V_code.objects.none()
    e_mail = request.GET.get('email')
    try:
        userobj = User.objects.get(email=e_mail)
    except User.DoesNotExist:
        return HttpResponse('invalid mail')
    if userobj:
        vcode = random.randint(100000, 999999)
        string = 'Enter verification code sent to you email'
        message = ('Your Verifaction code to reset password is : '+ str(vcode))
        try:
            ver_obj = V_code.objects.get(user=userobj)
        except V_code.DoesNotExist:
            V_code.objects.create(user=userobj,code=vcode)
        if ver_obj:
            string = 'Your verification code is updated'
            ver_obj.code = vcode
            ver_obj.save()
        # SENDING MAIL TO USER___---------
        flag = send_mail(
            'Password Recovery Code',
            message,
            'ecommerce.store.jpr@gmail.com',
            [e_mail],
            fail_silently=False,
        ) 
        string = string + "?" + e_mail
        return HttpResponse(string)


from jeneprocessor.jenepdf import JenePDF

def render_jene(request):
    pdf_config = JenePDF("test.html", "result.pdf")
    result = pdf_config.produce_pdf()
    return result



def send_recovery_code(request):
    v_code = request.GET.get('v_code')
    if v_code:
        mail = request.GET.get('mail')
        userobj = User.objects.get(email=mail)
        try:
            verobj = V_code.objects.get(user=userobj,code=v_code)
        except V_code.DoesNotExist:
            return HttpResponse("invalid Code")
        if verobj:
            verobj.delete()
            auth.login(request,userobj)
            return HttpResponse("logged inn")

    string = ''
    ver_obj = V_code.objects.none()
    e_mail = request.GET.get('email')
    try:
        userobj = User.objects.get(email=e_mail)
    except User.DoesNotExist:
        return HttpResponse('invalid mail')
    if userobj:
        vcode = random.randint(100000, 999999)
        string = 'Enter verification code sent to you email'
        message = ('Your Verifaction code to reset password is : '+ str(vcode))
        try:
            ver_obj = V_code.objects.get(user=userobj)
        except V_code.DoesNotExist:
            V_code.objects.create(user=userobj,code=vcode)
        if ver_obj:
            string = 'Your verification code is updated'
            ver_obj.code = vcode
            ver_obj.save()
        # SENDING MAIL TO USER___---------
        flag = send_mail(
            'Password Recovery Code',
            message,
            'ecommerce.store.jpr@gmail.com',
            [e_mail],
            fail_silently=False,
        ) 
        string = string + "?" + e_mail
        return HttpResponse(string)