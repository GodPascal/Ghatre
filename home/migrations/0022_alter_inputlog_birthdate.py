# Generated by Django 5.0.3 on 2024-05-24 13:14

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_inputlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputlog',
            name='birthdate',
            field=django_jalali.db.models.jDateField(blank=True, verbose_name='Birthdate'),
        ),
    ]