from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


# Create your models here.

class Users(AbstractBaseUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    objects = UserManager()
