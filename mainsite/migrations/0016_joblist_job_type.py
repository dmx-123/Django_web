# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-01 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0015_auto_20180101_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='job_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]