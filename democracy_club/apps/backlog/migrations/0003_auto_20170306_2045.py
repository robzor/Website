# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0002_auto_20170306_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardlabel',
            old_name='color',
            new_name='colour',
        ),
    ]
