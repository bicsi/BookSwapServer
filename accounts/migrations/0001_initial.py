# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 08:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('access_token', models.CharField(blank=True, default=None, max_length=511, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, default=None, max_length=255, null=True, validators=[django.core.validators.RegexValidator('male|female')])),
                ('email', models.EmailField(max_length=254)),
                ('social_update_time', models.DateTimeField(auto_now=True)),
                ('social_auth_method', models.CharField(blank=True, default=None, max_length=255, null=True, validators=[django.core.validators.RegexValidator('facebook')])),
                ('social_id', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
    ]
