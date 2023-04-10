from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


# Register your models here.
class CustomerAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ['date_joined']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserProfile)
admin.site.register(User, CustomerAdmin)