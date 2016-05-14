# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
