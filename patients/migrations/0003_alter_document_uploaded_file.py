# Generated by Django 5.0.3 on 2024-06-12 02:08

import private_storage.fields
import private_storage.storage.files
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_remove_patientcase_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_file',
            field=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='documents/', verbose_name='File'),
        ),
    ]
