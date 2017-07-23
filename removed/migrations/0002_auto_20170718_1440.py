# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 14:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('removed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='part_num',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='component',
            name='serial_num',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('\\d{8,8}', 'Must be 8 digit Serial Number', 'Invalid Number')]),
        ),
        migrations.AlterField(
            model_name='fixed_board',
            name='serial_num',
            field=models.PositiveIntegerField(max_length=8, validators=[django.core.validators.RegexValidator('\\d{8,8}', 'Must be 8 digit Serial Number', 'Invalid Number')]),
        ),
    ]