from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager
class User(AbstractUser):
    email = models.EmailField(max_length=1024, unique=True)
    username=None


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()
