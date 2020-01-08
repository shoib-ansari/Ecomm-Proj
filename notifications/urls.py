from django.urls import path
from .import views

#  ================== <<<<<<<<<<<<<<<    ALL URLs here    >>>>>>>>>  ========================================

urlpatterns = [
    path('',views.show_notifications,name="show all notifications"),
    path('mark_seen',views.mark_seen,name="mark_seen notification")
]