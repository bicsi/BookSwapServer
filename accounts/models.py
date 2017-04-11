from __future__ import unicode_literals

from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=255)
    access_token = models.CharField(
        max_length=511, null=True, default=None, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        validators=[RegexValidator('male|female')],
        max_length=255,
        null=True,
        blank=True,
        default=None)
    email = models.EmailField(blank=True, default=None)
    social_update_time = models.DateTimeField(auto_now=True)
    social_auth_method = models.CharField(
        validators=[RegexValidator('facebook')],
        null=True,
        blank=True,
        default=None,
        max_length=255)
    social_id = models.CharField(
        null=True, blank=True, default=None, max_length=255)

    def __str__(self):
        return self.username

admin.site.register(Account)
