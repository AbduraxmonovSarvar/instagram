# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]