from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from accounts.forms import Registerform
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


# User=get_user_model()


class UserAdmin(UserAdmin):
    # add_form = Registerform
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username','email', 'password1', 'password2','image','bio'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'image', 'bio')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', ),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# admin.site.unregister(User)
admin.site.register(UserModel, UserAdmin)