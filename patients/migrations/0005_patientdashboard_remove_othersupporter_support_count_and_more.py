# Generated by Django 5.0.3 on 2024-07-08 12:41

import datetime
import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_inputlog_description_and_more'),
        ('patients', '0004_remove_othersupporter_other_information_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDashboard',
            fields=[
            ],
            options={
                'verbose_name': 'Patient Dashboard',
                'verbose_name_plural': 'Patient Dashboards',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('patients.patientcase',),
        ),
        migrations.RemoveField(
            model_name='othersupporter',
            name='support_count',
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='national_code',
            field=models.CharField(max_length=12, verbose_name='National Code'),
        ),
        migrations.AlterField(
            model_name='applicationsupport',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='applicationsupport',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='applicationsupport',
            name='multiple_receive',
            field=models.BooleanField(default=True, verbose_name='Multiple Receive'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationsupport',
            name='prescription_cost',
            field=models.PositiveIntegerField(verbose_name='Prescription Cost'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='amount_of_installment_or_debt',
            field=models.PositiveIntegerField(verbose_name='Amount of Installment or Debt'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='deposit_amount',
            field=models.PositiveIntegerField(verbose_name='Deposit Amount'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='family_monthly_expenses',
            field=models.PositiveIntegerField(verbose_name='Family Monthly Expenses'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='has_job',
            field=models.BooleanField(default=True, verbose_name='Has Job'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='helper_assessment',
            field=models.TextField(verbose_name='Helper Assessment'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='helper_comment',
            field=models.TextField(verbose_name='Helper Comment'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='monthly_income',
            field=models.PositiveIntegerField(verbose_name='Monthly Income'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='other_monthly_income',
            field=models.PositiveIntegerField(default=0, verbose_name='Other Monthly Income'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='patient_problem',
            field=models.TextField(verbose_name='Patient Problem'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='rent_amount',
            field=models.PositiveIntegerField(verbose_name='Rent Amount'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='repayment_due_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='Repayment Due Date'),
        ),
        migrations.AlterField(
            model_name='livelihoodassessment',
            name='subsidy',
            field=models.PositiveIntegerField(verbose_name='Subsidy'),
        ),
        migrations.AlterField(
            model_name='othersupporter',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='othersupporter',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='othersupporter',
            name='support_amount',
            field=models.PositiveIntegerField(verbose_name='Support Amount'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='case_completion_date',
            field=django_jalali.db.models.jDateField(default=datetime.datetime.now, verbose_name='Case Completion Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.inputlog', verbose_name='Patient'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='representor',
            field=models.CharField(max_length=255, verbose_name='Representor'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='representor_phone',
            field=models.CharField(max_length=20, verbose_name='Representor Phone'),
        ),
        migrations.AlterField(
            model_name='patientcase',
            name='representor_relation',
            field=models.CharField(max_length=255, verbose_name='Representor Relation'),
        ),
        migrations.AlterField(
            model_name='patienthelperhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='patienthelperhistory',
            name='patient_description',
            field=models.TextField(blank=True, verbose_name='Patient Description'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='health_status',
            field=models.TextField(verbose_name='Health Status'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='monthly_income',
            field=models.PositiveIntegerField(verbose_name='Monthly Income'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='year_of_birth',
            field=models.PositiveIntegerField(verbose_name='Year of Birth'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='end_date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='percentage',
            field=models.PositiveIntegerField(verbose_name='Percentage'),
        ),
        migrations.AlterField(
            model_name='supportprogram',
            name='program_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Program Type'),
        ),
        migrations.CreateModel(
            name='CaseCompletionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modified At')),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('waiting_for_insurance ', 'Waiting for Insurance'), ('document_defects', 'Document Defects')], max_length=30, verbose_name='Status')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patientcase', verbose_name='Patient Case')),
            ],
            options={
                'verbose_name': 'Case Completion History',
                'verbose_name_plural': 'Case Completion Histories',
            },
        ),
    ]