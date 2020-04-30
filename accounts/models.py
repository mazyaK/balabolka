from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.safestring import mark_safe
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
    avatar = models.ImageField(upload_to='accounts/avatars/', null=True, blank=True)
    about_me = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def get_avatar(self):
        if not self.avatar:
            return '/accounts/avatars/default_no_avatar.png'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe(f'<img src="{self.get_avatar()}" width=50 height="60">')

    avatar_tag.short_description = 'avatar'












