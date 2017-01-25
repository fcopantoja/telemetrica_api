# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 19:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(blank=True, max_length=100)),
                ('site', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('lat', models.CharField(blank=True, max_length=100)),
                ('lng', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]