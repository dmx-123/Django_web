# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-01 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0014_joblist_isgetdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='salaryMean',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='salaryMedian',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='salaryStd',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='joblist',
            name='salaryVar',
            field=models.FloatField(null=True),
        ),
    ]
