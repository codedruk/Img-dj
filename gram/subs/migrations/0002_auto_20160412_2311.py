# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='user_rec',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
    ]
