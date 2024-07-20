from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('manufacturer', 'Manufacturer'),
        ('user', 'User'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

