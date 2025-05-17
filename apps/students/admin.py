from django.contrib import admin
from django.contrib.admin import ModelAdmin

from students.models import StudentJourney, Language, Student


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
    list_display = 'language', 'user',
    list_filter = 'language', 'user',
    search_fields = 'language', 'user',
    ordering = 'language',


@admin.register(Student)
class StudentModelAdmin(ModelAdmin):
    list_display = ('user', 'father_name', 'mother_name', 'birth_place', 'nationality', 'passport_series',
                    'passport_number', 'inn', 'address', 'phone_number', 'parent_phone_number', 'emergency_contact',
                    'uni_name', 'study_type', 'contract_number', 'photo')
    list_filter = 'uni_name', 'nationality', 'birth_place', 'study_type',
    search_fields = ('uni_name', 'nationality', 'birth_place', 'passport_series', 'passport_number',
                     'inn', 'phone_number',)
    ordering = 'inn',
