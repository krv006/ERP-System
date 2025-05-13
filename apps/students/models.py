from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, Model, JSONField, OneToOneField, CASCADE, \
    DateTimeField, DateField, TextField, ForeignKey
from django.db.models import Model
from django.utils import timezone


class Student(Model):
    user = OneToOneField('users.User', CASCADE)
    father_name = CharField(max_length=100)
    address = TextField()
    study_type = CharField(max_length=20, choices=[('full_time', 'Kunduzgi'), ('part_time', 'Sirtqi')])
    contract_number = CharField(max_length=20)

    def __str__(self):
        return self.user.full_name()


class StudentJourney(Model):
    STATUS_CHOICES = [
        ('admitted', 'Admitted'),  # Talaba qabul qilindi
        ('studying', 'Studying'),  # Talaba o‘qishda
        ('graduated', 'Graduated'),  # Talaba bitirdi
        ('employed', 'Employed'),  # Talaba ishga joylashgan
        ('frozen', 'Frozen'),  # Talaba muzlatilgan
        ('dropped_out', 'Dropped Out'),  # Talaba o‘qishni tark etdi
    ]

    student = OneToOneField('students.Student', CASCADE)
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


class Language(Model):
    language = CharField(max_length=50)
    language_grid = CharField(max_length=50, help_text='A1 or A2, B1 or B2 ...')
    user = ForeignKey('users.User', CASCADE, related_name='language_user')

    def __str__(self):
        return f'{self.language}'
