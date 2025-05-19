from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=12,blank=True,null=True)
    email = models.EmailField()
