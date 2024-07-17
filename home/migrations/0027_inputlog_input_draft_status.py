# Generated by Django 5.0.3 on 2024-07-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_inputlog_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputlog',
            name='input_draft_status',
            field=models.CharField(choices=[('identified', 'شناسایی شده'), ('evaluated', 'ارزیابی شده'), ('accepted', 'پذیرش'), ('rejected', 'عدم پذیرش'), ('waiting', 'در انتظار')], default='waiting', max_length=30, verbose_name='Input Draft Status'),
        ),
    ]