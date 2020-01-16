from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('logut',views.logout,name='LOGOUT'),
    path('register',views.register,name='Register a user'),
    path('manage_address',views.addr_page,name='Display manage address page'),
    path('update_addr',views.update_addr,name='update address of user'),
    path('update_user_profile',views.update_profile,name='Update user profile'),
    path('userprofile',views.update_user_profile_page,name='Display Page for update userprofile'),
    path('checkuserlogin',views.checklogin,name='checkinguserlogin'),
    path('test',views.test,name='checkinguserlogin'),
    path('forgot_pwd',views.f_p_page,name='Open Forgot pwd page'),
    path('send_recovery',views.send_recovery,name='Send recovery mail')
]