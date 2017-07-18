# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 15:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('removed', '0003_auto_20170718_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='part_num',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('.{8,}', 'Must be at least 8 characters')]),
        ),
        migrations.AlterField(
            model_name='component',
            name='serial_num',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('\\d{8}', 'Must be 8 digit Serial Number', 'Invalid Number')]),
        ),
        migrations.AlterField(
            model_name='fixed_board',
            name='serial_num',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('\\d{8}', 'Must be 8 digit Serial Number', 'Invalid Number')]),
        ),
    ]
