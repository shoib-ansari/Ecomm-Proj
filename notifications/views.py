from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.


def show_notifications(request):
    notiobj = Notifications.objects.filter(user=request.user)
    return render(request,'notifications.html',{"notification":notiobj})

def mark_seen(request):
    n_id = request.GET.get('n_id')
    if n_id:
        try :
            notiobj = Notifications.objects.get(id=n_id,user=request.user)
        except Notifications.DoesNotExist:
            return HttpResponse("Error")

        notiobj.seen_by_user = True
        notiobj.save()
        return HttpResponse("success")
    else:
        notiobj = Notifications.objects.filter(user=request.user).update(seen_by_user = True)
        # notiobj.seen_by_user = True
        # notiobj.save()
        return HttpResponse("success")