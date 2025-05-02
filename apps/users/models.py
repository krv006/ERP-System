from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, BooleanField, Model, JSONField, OneToOneField, CASCADE, \
    DateTimeField, DateField, TextField
from django.utils import timezone

from users.managers import CustomUserManager


class User(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'SuperAdmin'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('coordinator', 'Coordinator'),
        ('operator', 'Operator'),
        ('reception', 'Reception'),
        ('teacher', 'Teacher'),
        ('assistant_teacher', 'Assistant Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('marketing', 'Marketing'),
        ('content_creator', 'Content Creator'),
        ('designer', 'Designer'),
        ('seo_specialist', 'SEO Specialist'),
        ('accountant', 'Accountant'),
        ('hr', 'HR'),
        ('it_support', 'IT Support'),
        ('security', 'Security'),
        ('dev', 'Developer'),
        ('intern', 'Intern'),
    ]
    role = CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    first_name = CharField(max_length=150, blank=True)
    last_name = CharField(max_length=150, blank=True)

    email = EmailField(unique=True)
    is_active = BooleanField(default=False)

    # todo Talaba haqida qo‘shimcha ma'lumotlar
    date_of_birth = DateField(null=True, blank=True)
    phone_number = CharField(max_length=15, blank=True, null=True)
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} - {self.username}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class StudentJourney(Model):
    STATUS_CHOICES = [
        ('admitted', 'Admitted'),  # Talaba qabul qilindi
        ('studying', 'Studying'),  # Talaba o‘qishda
        ('graduated', 'Graduated'),  # Talaba bitirdi
        ('employed', 'Employed'),  # Talaba ishga joylashgan
        ('frozen', 'Frozen'),  # Talaba muzlatilgan
        ('dropped_out', 'Dropped Out'),  # Talaba o‘qishni tark etdi
    ]

    user = OneToOneField('users.User', CASCADE, limit_choices_to={'role': 'student'})
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='admitted')
    enrollment_date = DateTimeField(default=timezone.now)  # Qabul qilingan sana
    graduation_date = DateField(null=True, blank=True)  # Bitirish sanasi
    employment_status = BooleanField(default=False)  # Ishga joylashgan yoki yo‘qligini ko‘rsatadi
    frozen_reason = TextField(blank=True, null=True)  # Muzlatilgan bo‘lsa, sababi
    dropout_reason = TextField(blank=True, null=True)  # Tark etish sababi

    # Davomat tarixini kuzatish
    attendance = JSONField(default=list, blank=True)  # Davomat (ro‘yxat sifatida)

    # Ishga joylashish jarayoni
    job_search_status = BooleanField(default=False)  # Ish qidirish holati
    job_offer_received = BooleanField(default=False)  # Ish taklifini olish holati
    job_offer_accepted = BooleanField(default=False)  # Ishga joylashganligini tasdiqlash

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - Status: {self.get_status_display()}'

    def is_active(self):
        return self.status == 'studying'

    def is_employed(self):
        return self.status == 'employed'

    def complete_employment(self):
        self.status = 'employed'
        self.employment_status = True
        self.save()

    def freeze(self, reason):
        self.status = 'frozen'
        self.frozen_reason = reason
        self.save()

    def drop_out(self, reason):
        self.status = 'dropped_out'
        self.dropout_reason = reason
        self.save()

    def mark_attendance(self, date, is_present):
        # Davomatni belgilash
        self.attendance.append({"date": date, "is_present": is_present})
        self.save()
