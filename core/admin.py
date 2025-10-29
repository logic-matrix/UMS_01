from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')

    def has_change_permission(self, request, obj=None):
        # only super_admin can edit users
        return request.user.role == 'super_admin'

    def has_view_permission(self, request, obj=None):
        # admins and super_admin can view users
        return request.user.role in ['admin', 'super_admin']

admin.site.register(User, UserAdmin)
