from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ['email','first_name','last_name','is_staff','is_superuser','role','last_login']

admin.site.register(CustomUser,UserAdmin)