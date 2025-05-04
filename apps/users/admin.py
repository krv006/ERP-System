from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, StudentJourney


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Shaxsiy Maʼlumotlar', {'fields': ()}),
        ('Ruxsatlar', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Muhim sanalar', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )
    search_fields = 'email',
    ordering = 'email',


admin.site.register(User, UserAdmin)


@admin.register(StudentJourney)
class StudentJourneyModelAdmin(ModelAdmin):
    pass