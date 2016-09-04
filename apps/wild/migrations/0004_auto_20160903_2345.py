# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wild', '0003_auto_20160903_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplace',
            name='place_id',
        ),
        migrations.AddField(
            model_name='userplace',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userplace',
            name='place_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
