# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-04 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='founder',
            name='alt_email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='pro_com',
            field=models.BooleanField(default=False, verbose_name='pro com'),
        ),
    ]
