from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('logut',views.logout,name='LOGOUT'),
    path('register',views.register,name='Register a user'),
    path('checkuserlogin',views.checklogin,name='checkinguserlogin')
]