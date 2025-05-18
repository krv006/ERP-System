from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, Model, JSONField, OneToOneField, CASCADE, \
    DateField, TextField, ForeignKey, ImageField
from django.db.models import Model
from django.utils import timezone


class Address(Model):
    country = CharField(max_length=100, default='Uzbekistan')
    region = CharField(max_length=255)
    city = CharField(max_length=255)
    district = CharField(max_length=255, blank=True, null=True)
    street = CharField(max_length=255, blank=True, null=True)
    house_number = CharField(max_length=20, blank=True, null=True)
    postal_code = CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.region}, {self.city}"


# Hamma alohida entitilar alohida bo‘lsa, normalized bo‘ladi

class Student(Model):
    # Basic info
    user = OneToOneField('users.User', CASCADE, related_name='student_profile')
    photo = ImageField(blank=True, null=True)
    address = ForeignKey(Address, CASCADE, related_name='students')

    # Family info
    father_name = CharField(max_length=100)
    mother_name = CharField(max_length=100, blank=True, null=True)
    parent_phone_number = CharField(max_length=55, blank=True, null=True)
    emergency_contact = CharField(max_length=15, blank=True, null=True)

    # Passport
    passport_series = CharField(max_length=10, blank=True, null=True)
    passport_number = CharField(max_length=20, blank=True, null=True)
    inn = CharField(max_length=14, blank=True, null=True)
    nationality = CharField(max_length=50, default="Uzbek")

    # Contact
    phone_number = CharField(max_length=55, blank=True, null=True)
    telegram = CharField(max_length=100, blank=True, null=True)
    email = CharField(max_length=100, blank=True, null=True)
    github_link = CharField(max_length=255, blank=True, null=True)

    # Education
    birth_place = CharField(max_length=100, blank=True, null=True)
    uni_name = CharField(max_length=100, blank=True, null=True)
    study_type = CharField(max_length=20, choices=[
        ('full_time', 'Kunduzgi'),
        ('part_time', 'Sirtqi'),
        ('evening', 'Kechki')
    ])

    # Contract
    contract_number = CharField(max_length=20, unique=True)
    start_year = DateField(null=True, blank=True)
    expected_graduation_date = DateField(null=True, blank=True)
    actual_exit_date = DateField(null=True, blank=True)
    payment_status = CharField(max_length=20, choices=[
        ('paid', 'To‘langan'),
        ('unpaid', 'To‘lanmagan'),
        ('debt', 'Qarzdor')
    ], default='unpaid')

    def __str__(self):
        return self.user.full_name()


class StudentJourney(Model):
    STATUS_CHOICES = [
        ('admitted', 'Qabul qilindi'),
        ('studying', 'O‘qishda'),
        ('graduated', 'Bitirdi'),
        ('employed', 'Ishga joylashgan'),
        ('frozen', 'Muzlatilgan'),
        ('dropped_out', 'Tark etdi'),
    ]

    DEMO_STATUS = [
        ('not_started', 'Boshlanmagan'),
        ('in_progress', 'Jarayonda'),
        ('completed', 'Yakunlangan'),
    ]

    student = OneToOneField(Student, CASCADE, related_name='journey')

    status = CharField(max_length=20, choices=STATUS_CHOICES, default='admitted')
    enrollment_date = DateField(default=timezone.now)
    graduation_date = DateField(null=True, blank=True)
    frozen_reason = TextField(blank=True, null=True)
    dropout_reason = TextField(blank=True, null=True)

    # Academic progress
    midterm_score = CharField(max_length=10, blank=True, null=True)
    final_score = CharField(max_length=10, blank=True, null=True)
    homework_score = CharField(max_length=10, blank=True, null=True)
    demo_project_status = CharField(max_length=50, choices=DEMO_STATUS, blank=True, null=True)

    # Attendance
    attendance = JSONField(default=list, blank=True)

    # Employment
    job_search_status = BooleanField(default=False)
    job_offer_received = BooleanField(default=False)
    job_offer_accepted = BooleanField(default=False)
    employment_status = BooleanField(default=False)
    internship_company = CharField(max_length=100, blank=True, null=True)
    job_company = CharField(max_length=100, blank=True, null=True)
    job_title = CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.full_name()} - {self.get_status_display()}"

    def is_active(self):
        return self.status == 'studying'

    def mark_attendance(self, date, is_present):
        self.attendance.append({
            "date": str(date),
            "is_present": is_present
        })
        self.save()


class Language(Model):
    language = CharField(max_length=50)
    language_level = CharField(max_length=10, help_text='A1, A2, B1, B2, C1, C2')
    user = ForeignKey('users.User', CASCADE, related_name='languages')
    certificate_name = CharField(max_length=100, blank=True, null=True)
    certificate_score = CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.language} - {self.language_level}'
