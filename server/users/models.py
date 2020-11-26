from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager
class User(AbstractUser):
    email = models.EmailField(max_length=1024, unique=True)
    first_name = models.CharField(max_length=1024, default="")
    username=None

    USER_TYPES = [
        ('MT', 'Mentee'),
        ('MR', 'Mentor')
    ]
    duration = models.CharField(max_length=2, default='3')
    qualification = models.CharField(
        max_length=10, 
        blank=True, 
        default="Student"
    )

    user_type = models.CharField(
        max_length=2,
        blank=True,
        default='MT'
    )

    organization = models.CharField(
        max_length=1024, 
        blank=True, 
        default=""
    )
    requirement = models.CharField(
        max_length=1024, 
        blank=True, 
        default=""
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()
