from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display =('username','last_name', 'first_name','middle_name','email', 'phone',)
    list_filter = ('username','last_name', 'first_name','middle_name','email', 'phone',)
    search_fields =('username','last_name', 'first_name','middle_name','email', 'phone',)