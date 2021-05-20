from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ('username', 'name')


admin.site.register(User, UserAdmin)
