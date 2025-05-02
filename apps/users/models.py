from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, BooleanField

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
    username = CharField(max_length=150, unique=True)
    first_name = CharField(max_length=150, blank=True)
    last_name = CharField(max_length=150, blank=True)

    email = EmailField(unique=True)
    is_active = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} - {self.username}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
