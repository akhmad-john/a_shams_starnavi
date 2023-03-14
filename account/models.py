from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampMixin


class User(TimeStampMixin, AbstractUser):
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    last_request = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

