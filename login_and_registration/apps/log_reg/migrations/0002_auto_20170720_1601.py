# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
