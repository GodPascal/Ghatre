# Generated by Django 5.0.3 on 2024-04-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_othersupporter_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AddField(
            model_name='patientcase',
            name='helper_comment',
            field=models.TextField(blank=True, verbose_name='Helper Comment'),
        ),
        migrations.AddField(
            model_name='patientcase',
            name='patient_problem',
            field=models.TextField(blank=True, verbose_name='Patient Problem'),
        ),
    ]
