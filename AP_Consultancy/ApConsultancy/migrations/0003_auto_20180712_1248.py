# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApConsultancy', '0002_auto_20180712_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeruser',
            old_name='emailId',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registeruser',
            old_name='jobType',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='registeruser',
            old_name='mobileNumber',
            new_name='mobile',
        ),
    ]
