from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('useraccounts.urls')),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls')),
    path('orderprocessing/',include('orderprocessing.urls')),
    path('notifications/',include('notifications.urls')),
    path('offers/',include('offers.urls')),
    path('accounts/',include('allauth.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)