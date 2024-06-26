# Generated by Django 5.0.3 on 2024-05-09 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_drugbrand_genericdrug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('usage_start', models.CharField(max_length=30, verbose_name='Usage Start')),
                ('usage_duration', models.CharField(max_length=30, verbose_name='Usage Duration')),
                ('usage_instruction', models.CharField(max_length=30, verbose_name='Usage Instruction')),
                ('costs', models.IntegerField(blank=True, null=True, verbose_name='Costs')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('drug_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.drugbrand', verbose_name='Drug Brand')),
                ('generic_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.genericdrug', verbose_name='Generic Drug')),
                ('patient_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.patientcase', verbose_name='Patient Case')),
            ],
            options={
                'verbose_name': 'Patient Drug',
                'verbose_name_plural': 'Patient Drugs',
            },
        ),
    ]
