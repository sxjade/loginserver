# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161205_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userctpaccount',
            name='id',
        ),
        migrations.AlterField(
            model_name='userctpaccount',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.User'),
        ),
    ]
