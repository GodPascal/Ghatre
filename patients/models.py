from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from private_storage.fields import PrivateFileField

from home.models import BaseModel, InputLog
from utils.consts import GENDER_CHOICES, NATIONALITY_CHOICES, GUARDIAN_STATUS_CHOICES, SOCIAL_INSURANCE_TYPE_CHOICES, \
    EDUCATIONAL_STATUS_CHOICES, MARITAL_STATUS_CHOICES, HOUSING_STATUS_CHOICES, DOCUMENT_TYPE_CHOICES, \
    PATIENT_CASE_STATUS_CHOICES, RECIPIENT_CHOICES, INTERVAL_CHOICES, SUPPORT_PROGRAM_CHOICES, DELIVERY_TYPE_CHOICES, \
    PATIENT_DRUG_STATUS_CHOICES, COMPLETION_CASE_CHOICES


class PatientCase(BaseModel):
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    patient = models.OneToOneField(InputLog, on_delete=models.SET_NULL, null=True, verbose_name=_('Patient'))
    status = models.CharField(max_length=20, choices=PATIENT_CASE_STATUS_CHOICES, verbose_name=_('Status'))
    case_number = models.CharField(max_length=255, verbose_name=_('Case Number'))
    case_completion_date = jmodels.jDateField(verbose_name=_('Case Completion Date'))
    father_name = models.CharField(max_length=255, verbose_name=_('Father Name'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    birthdate = jmodels.jDateField(verbose_name=_('Birthdate'))
    national_code = models.CharField(max_length=12, verbose_name=_('National Code'))
    nationality = models.CharField(max_length=10, choices=NATIONALITY_CHOICES, verbose_name=_('Nationality'))

    guardian_status = models.CharField(max_length=10, choices=GUARDIAN_STATUS_CHOICES,
                                       verbose_name=_('Guardian Status'))
    first_guardian_name = models.CharField(max_length=255, blank=True, verbose_name=_('First Guardian Name'))
    first_guardian_national_code = models.CharField(max_length=10, blank=True,
                                                    verbose_name=_('First Guardian National Code'))
    first_guardian_relation = models.CharField(max_length=255, blank=True, verbose_name=_('First Guardian Relation'))
    second_guardian_name = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Name'))
    second_guardian_national_code = models.CharField(max_length=10, blank=True,
                                                     verbose_name=_('Second Guardian National Code'))
    second_guardian_relation = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Relation'))

    social_insurance_type = models.CharField(max_length=255, choices=SOCIAL_INSURANCE_TYPE_CHOICES,
                                             verbose_name=_('Social Insurance Type'))
    social_insurance_description = models.TextField(blank=True, verbose_name=_('Social Insurance Description'))

    educational_status = models.CharField(max_length=20, choices=EDUCATIONAL_STATUS_CHOICES,
                                          verbose_name=_('Educational Status'))

    private_insurance_name = models.CharField(max_length=255, blank=True, verbose_name=_('Private Insurance Name'))
    private_insurance_description = models.TextField(blank=True, verbose_name=_('Private Insurance Description'))

    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    marital_status_description = models.TextField(blank=True, verbose_name=_('Marital Status Description'))
    
    address = models.TextField(blank=True, verbose_name=_('Address'))
    home_number = models.CharField(max_length=20, verbose_name=_('Home Number'))
    
    representor = models.CharField(max_length=255, verbose_name=_('Representor'))
    representor_relation = models.CharField(max_length=255, verbose_name=_('Representor Relation'))
    representor_phone = models.CharField(max_length=20, verbose_name=_('Representor Phone'))
    other_information = models.TextField(blank=True, verbose_name=_('Other Information'))
    description = models.TextField(blank=True, verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Patient Case')
        verbose_name_plural = _('Patient Cases')

    def __str__(self) -> str:
        return '%s       %s' % (self.first_name, self.last_name)
    
    @property
    def first_name(self):
        if self.patient:
            return self.patient.first_name

    @property
    def last_name(self):
        if self.patient:
            return self.patient.last_name
    
    @property
    def full_name(self):
        if self.patient:
            return f'{self.patient.first_name} {self.patient.last_name}' 

    @property
    def phone_number(self):
        if self.patient:
            return self.patient.phone_number
    
    @property
    def patient_final_payment(self):
        return self.applicationsupport_set.all().aggregate(Sum(
            'prescription_cost')).get('prescription_cost__sum') or 0
        
    last_name.fget.short_description = _('Last Name')
    first_name.fget.short_description = _('First Name')
    phone_number.fget.short_description = _('Phone Number')


class PatientDashboard(PatientCase):
    class Meta:
        proxy = True
        verbose_name = _('Patient Dashboard')
        verbose_name_plural = _('Patient Dashboards')


class CaseCompletionHistory(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    status = models.CharField(max_length=30, choices=COMPLETION_CASE_CHOICES, verbose_name=_('Status'))
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        verbose_name = _('Case Completion History')
        verbose_name_plural = _('Case Completion Histories')

    def __str__(self) -> str:
        return f'{self.pk}'


class Document(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES, verbose_name=_('Type'))
    uploaded_file = PrivateFileField(upload_to='documents/', verbose_name=_('File'))

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self) -> str:
        return f'{self.pk}'

class LivelihoodAssessment(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    housing_status = models.CharField(max_length=20, choices=HOUSING_STATUS_CHOICES, verbose_name=_('Housing Status'))
    deposit_amount = models.PositiveIntegerField(verbose_name=_('Deposit Amount'))
    rent_amount = models.PositiveIntegerField(verbose_name=_('Rent Amount'))

    has_job = models.BooleanField(verbose_name=_('Has Job'))
    job_description = models.TextField(blank=True, verbose_name=_('Job Description'))
    monthly_income = models.PositiveIntegerField(verbose_name=_('Monthly Income'))
    other_monthly_income = models.PositiveIntegerField(default=0, verbose_name=_('Other Monthly Income'))
    subsidy = models.PositiveIntegerField(verbose_name=_('Subsidy'))
    family_monthly_expenses = models.PositiveIntegerField(verbose_name=_('Family Monthly Expenses'))
    amount_of_installment_or_debt = models.PositiveIntegerField(verbose_name=_('Amount of Installment or Debt'))
    repayment_due_date = jmodels.jDateField(verbose_name=_('Repayment Due Date'), null=True, blank=True)
    income_expenses_description = models.TextField(blank=True, verbose_name=_('Income Expenses Description'))
    
    recipient = models.CharField(max_length=10, choices=RECIPIENT_CHOICES, verbose_name=_('Recipient'))
    patient_problem = models.TextField(verbose_name=_('Patient Problem'))
    helper_comment = models.TextField(verbose_name=_('Helper Comment'))
    helper_assessment = models.TextField(verbose_name=_('Helper Assessment'))

    class Meta:
        verbose_name = _('Livelihood Assessment')
        verbose_name_plural = _('Livelihood Assessments')

    def __str__(self) -> str:
        return f'{self.pk}'


class Relative(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    first_name = models.CharField(max_length=255, blank=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, blank=True, verbose_name=_('Last Name'))
    relation = models.CharField(max_length=255, verbose_name=_('Relation'))
    year_of_birth = models.PositiveIntegerField(verbose_name=_('Year of Birth'))
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    occupation = models.CharField(max_length=255, verbose_name=_('Occupation'))
    monthly_income = models.PositiveIntegerField(verbose_name=_('Monthly Income'))
    health_status = models.TextField(verbose_name=_('Health Status'))

    class Meta:
        verbose_name = _('Relative')
        verbose_name_plural = _('Relatives')

    def __str__(self) -> str:
        return f'{self.pk}'


class OtherSupporter(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    is_active = models.BooleanField(null=True, verbose_name=_('Active'))
    name = models.CharField(max_length=255, blank=True, verbose_name=_('Name'))
    support_amount = models.PositiveIntegerField(verbose_name=_('Support Amount'))
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Other Supporter')
        verbose_name_plural = _('Other Supporters')

    def __str__(self) -> str:
        return f'{self.pk}'


class ApplicationSupport(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    multiple_receive = models.BooleanField(verbose_name=_('Multiple Receive'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))
    first_intake_date = jmodels.jDateField(verbose_name=_('First Intake Date'))
    prescription_cost = models.PositiveIntegerField(verbose_name=_('Prescription Cost'))
    help_intervals = models.CharField(max_length=20, choices=INTERVAL_CHOICES, verbose_name=_('Help Intervals'))
    supplier_pharmacy = models.CharField(max_length=255, verbose_name=_('Supplier Pharmacy'))
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Application Support')
        verbose_name_plural = _('Application Supports')

    def __str__(self) -> str:
        return f'{self.pk}'


class SupportProgram(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    percentage = models.PositiveIntegerField(verbose_name=_('Percentage'))
    amount = models.PositiveIntegerField(verbose_name=_('Amount'))
    intervals = models.CharField(max_length=255, verbose_name=_('Intervals'))
    count = models.IntegerField(verbose_name=_('Count'))
    end_date = jmodels.jDateField(null=True, blank=True, verbose_name=_('End Date'))
    support_program = models.CharField(max_length=20, choices=SUPPORT_PROGRAM_CHOICES, verbose_name=_('Support Program'))
    program_type = models.CharField(max_length=255, blank=True, verbose_name=_('Program Type'))
    service_pharmacy = models.CharField(max_length=255, verbose_name=_('Service Pharmacy'))
    drug_delivery_type = models.CharField(max_length=20, choices= DELIVERY_TYPE_CHOICES, verbose_name=_('Drug Delivery Type'))
    status = models.CharField(max_length=20, choices=PATIENT_DRUG_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Support Program')
        verbose_name_plural = _('Support Programs')

    def __str__(self) -> str:
        return f'{self.pk}'
    
    @property
    def total_other_support(self):
        if not SupportProgram.objects.filter(patient_case=self.patient_case,
                                             created_at__lte=self.created_at).exclude(pk=self.pk).exists():
            return OtherSupporter.objects.filter(patient_case=self.patient_case).aggregate(
                Sum('support_amount')).get('support_amount__sum') or 0

        return 0
    
    total_other_support.fget.short_description = _('Total Other Support')


class PatientHelperHistory(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    
    patient_description = models.TextField(blank=True, verbose_name=_('Patient Description'))

    class Meta:
        verbose_name = _('Patient Helper History')
        verbose_name_plural = _('Patient Helper Histories')


    def __str__(self) -> str:
        return f'{self.pk}'
