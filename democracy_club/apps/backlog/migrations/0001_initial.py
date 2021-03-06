# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('trello_id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=800)),
                ('text', models.TextField(blank=True)),
                ('weight', models.FloatField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardLabel',
            fields=[
                ('trello_id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='labels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlog.CardLabel'),
        ),
    ]
