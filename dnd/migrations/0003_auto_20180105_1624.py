# Generated by Django 2.0.1 on 2018-01-05 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0002_auto_20180105_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerchar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL),
        ),
    ]
