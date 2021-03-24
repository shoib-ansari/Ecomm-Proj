from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username","is_superuser","is_staff","is_active","last_login","date_joined","contact")
    list_editable = ['is_superuser']
    list_display_links = ['is_staff']

admin.site.register(User,UserAdmin)

