from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from products.models import *
from cart.models import Cart


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
    print(product_dict)
    return product_dict


def homepage(request):
    
    product_dict = getnavitems(request)
    return render(request, "index.html",{"products":product_dict})
    

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



