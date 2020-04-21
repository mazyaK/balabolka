from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='accounts/avatars/', null=True, blank=True)
    about_me = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)








