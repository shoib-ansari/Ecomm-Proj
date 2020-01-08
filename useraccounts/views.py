from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse , HttpResponse
from .models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from products.models import *
from cart.models import Cart
import json
from notifications.models import Notifications


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
                        temp_final_list.append(k.name)
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


def homepage(request):
    
    product_dict = getnavitems(request)
    noti_flag = get_noti_status(request)
    return render(request, "index.html",{"products":product_dict,"notification":noti_flag})
    

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
