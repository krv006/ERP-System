from django.contrib import admin
from django.contrib.admin import ModelAdmin

from students.models import StudentJourney, Language


@admin.register(StudentJourney)
class StudentJourneyModelAdmin(ModelAdmin):
    list_display = 'student', 'status', 'enrollment_date', 'employment_status',
    list_filter = 'status', 'enrollment_date', 'employment_status',
    search_fields = 'student', 'status', 'enrollment_date', 'employment_status',
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
