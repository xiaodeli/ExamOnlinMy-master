# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-07 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180207_1450'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserClass',
        ),
    ]
