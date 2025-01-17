from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)