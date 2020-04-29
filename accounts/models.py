from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.text import slugify

username_validator = UnicodeUsernameValidator()

class User(AbstractUser):
    username = models.CharField(
        ('Username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    avatar = models.ImageField(upload_to='accounts/avatars/', default='/accounts/avatars/default_no_avatar.png', null=True, blank=True)
    about_me = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, default=slugify(username))










