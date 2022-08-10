from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, null=True, verbose_name='first name')
    last_name = models.CharField(max_length=200, null=True, verbose_name='last name')
    avatar = models.ImageField(null=True, default= "avatar.svg")
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name+" "+self.last_name