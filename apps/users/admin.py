from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, StudentJourney, Language


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


@admin.register(StudentJourney)
class StudentJourneyModelAdmin(ModelAdmin):
    list_display = 'user', 'status', 'enrollment_date', 'employment_status',
    list_filter = 'status', 'enrollment_date', 'employment_status',
    search_fields = 'user', 'status', 'enrollment_date', 'employment_status',
    ordering = 'employment_status',

    # fieldsets = (
    #     (None, {'fields': ('user', 'status')}),
    #     ('Status', {'fields': ('enrollment_date', 'employment_status')}),
    # )
    # todo admindan qoshimcha narsa chiqarish yani fieldsets mana shu ichida bergan narsalari alohida
    # TODO LEKIN MASLAHAT BERMAYMAN


@admin.register(Language)
class LanguageModelAdmin(ModelAdmin):
    list_display = 'language', 'language_grid', 'user',
    list_filter = 'language', 'language_grid', 'user',
    search_fields = 'language', 'user',
    ordering = 'language',


admin.site.register(User, UserAdmin)
