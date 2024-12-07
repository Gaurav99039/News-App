from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm,CustomUserChangeFrom
from .models import CustomUser
class CustomUserAdmin(UserAdmin): 
    add_form = CustomCreationForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ] # new 
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
