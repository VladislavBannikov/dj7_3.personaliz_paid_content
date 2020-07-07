# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_subscribed = models.BooleanField(default=False)


#
# class Profile(models.Model):
#     pass


class Article(models.Model):
    is_require_subscription = models.BooleanField(default=False)
    title = models.CharField(null=False, max_length=50, blank=False, verbose_name="title")
    image = models.ImageField(null=True, blank=True,     verbose_name="image")
    text = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


