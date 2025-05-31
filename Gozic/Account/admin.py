from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class CustomUserAdmin(UserAdmin):
    model = Account
    add_form = UserCreationForm
    form = UserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'birthday', 'position', 'location', 'company', 'skype', 'image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'birthday', 'position', 'location', 'company', 'skype', 'image')}),
    )

admin.site.register(Account, CustomUserAdmin)
