# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('removed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixed_board',
            name='notes',
            field=models.CharField(max_length=200),
        ),
    ]