from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

from home.models import BaseModel
from utils.consts import GENDER_CHOICES, NATIONALITY_CHOICES, GUARDIAN_STATUS_CHOICES, SOCIAL_INSURANCE_TYPE_CHOICES, \
    EDUCATIONAL_STATUS_CHOICES, MARITAL_STATUS_CHOICES, HOUSING_STATUS_CHOICES, PROVINCES_OF_IRAN_CHOICES, \
    DOCUMENT_TYPE_CHOICES


class PatientCase(BaseModel):
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    case_number = models.CharField(max_length=255, blank=True, verbose_name=_('Case Number'))
    refer_date = jmodels.jDateField(verbose_name=_('Refer Date'), blank=True, null=True)
    case_completion_date = jmodels.jDateField(verbose_name=_('Case Completion Date'), blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    father_name = models.CharField(max_length=255, verbose_name=_('Father Name'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    birthdate = jmodels.jDateField(verbose_name=_('Birthdate'))
    national_code = models.CharField(max_length=10, verbose_name=_('National Code'))
    nationality = models.CharField(max_length=10, choices=NATIONALITY_CHOICES, verbose_name=_('Nationality'))
    referrer_name = models.CharField(max_length=255, verbose_name=_('Referrer Name'))

    guardian_status = models.CharField(max_length=10, choices=GUARDIAN_STATUS_CHOICES,
                                       verbose_name=_('Guardian Status'))
    first_guardian_name = models.CharField(max_length=255, verbose_name=_('First Guardian Name'))
    first_guardian_national_code = models.CharField(max_length=10, blank=True,
                                                    verbose_name=_('First Guardian National Code'))
    first_guardian_relation = models.CharField(max_length=255, verbose_name=_('First Guardian Relation'))
    second_guardian_name = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Name'))
    second_guardian_national_code = models.CharField(max_length=10, blank=True,
                                                     verbose_name=_('Second Guardian National Code'))
    second_guardian_relation = models.CharField(max_length=255, blank=True, verbose_name=_('Second Guardian Relation'))

    social_insurance_type = models.CharField(max_length=255, choices=SOCIAL_INSURANCE_TYPE_CHOICES,
                                             verbose_name=_('Social Insurance Type'))
    social_insurance_description = models.TextField(blank=True, verbose_name=_('Social Insurance Description'))

    educational_status = models.CharField(max_length=20, choices=EDUCATIONAL_STATUS_CHOICES,
                                          verbose_name=_('Educational Status'))

    has_private_insurance = models.BooleanField(verbose_name=_('Has Private Insurance'))
    private_insurance_name = models.TextField(blank=True, verbose_name=_('Private Insurance Name'))
    private_insurance_number = models.CharField(max_length=255, blank=True, verbose_name=_('Private Insurance Number'))

    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    marital_status_description = models.TextField(blank=True, verbose_name=_('Marital Status Description'))

    housing_status = models.CharField(max_length=20, choices=HOUSING_STATUS_CHOICES, verbose_name=_('Housing Status'))
    deposit_amount = models.IntegerField(blank=True, null=True, verbose_name=_('Deposit Amount'))
    rent_amount = models.IntegerField(blank=True, null=True, verbose_name=_('Rent Amount'))

    has_job = models.BooleanField(null=True, verbose_name=_('Has Job'))
    job_description = models.TextField(blank=True, verbose_name=_('Job Description'))
    monthly_income = models.IntegerField(verbose_name=_('Monthly Income'))
    subsidy = models.IntegerField(verbose_name=_('Subsidy'))
    family_monthly_expenses = models.IntegerField(verbose_name=_('Family Monthly Expenses'))
    amount_of_installment_or_debt = models.IntegerField(verbose_name=_('Amount of Installment or Debt'))
    repayment_due_date = jmodels.jDateField(verbose_name=_('Repayment Due Date'))
    income_expenses_description = models.TextField(blank=True, verbose_name=_('Income Expenses Description'))

    province_of_residence = models.CharField(max_length=30, choices=PROVINCES_OF_IRAN_CHOICES, blank=True,
                                             verbose_name=_('Province of Residence'))
    city_of_residence = models.CharField(max_length=255, blank=True, verbose_name=_('City of Residence'))
    address = models.TextField(blank=True, verbose_name=_('Address'))

    mobile_number = models.CharField(max_length=20, verbose_name=_('Mobile Number'))
    phone_number = models.CharField(max_length=20, blank=True, verbose_name=_('Phone Number'))

    representor = models.CharField(max_length=255, verbose_name=_('Representor'))
    representor_relation = models.CharField(max_length=255, verbose_name=_('Representor Relation'))

    referrer_name = models.CharField(max_length=255, verbose_name=_('Referrer Name'))

    other_information = models.TextField(blank=True, verbose_name=_('Other Information'))

    patient_problem = models.TextField(blank=True, verbose_name=_('Patient Problem'))
    helper_comment = models.TextField(blank=True, verbose_name=_('Helper Comment'))

    class Meta:
        verbose_name = _('Patient Case')
        verbose_name_plural = _('Patient Cases')

    def __str__(self) -> str:
        return '%s       %s' % (self.first_name, self.last_name)


class Relative(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    relation = models.CharField(max_length=255, verbose_name=_('Relation'))
    year_of_birth = models.IntegerField(verbose_name=_('Year of Birth'))
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Marital Status'))
    occupation = models.CharField(max_length=255, verbose_name=_('Occupation'))
    monthly_income = models.IntegerField(verbose_name=_('Monthly Income'))
    health_status = models.CharField(max_length=255, verbose_name=_('Health Status'))

    class Meta:
        verbose_name = _('Relative')
        verbose_name_plural = _('Relatives')


class OtherSupporter(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    support_amount = models.IntegerField(verbose_name=_('Support Amount'))
    support_start = jmodels.jDateField(verbose_name=_('Support Start'))
    support_end = jmodels.jDateField(verbose_name=_('Support End'))
    other_information = models.TextField(blank=True, verbose_name=_('Other Information'))

    class Meta:
        verbose_name = _('Other Supporter')
        verbose_name_plural = _('Other Supporters')


class Document(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES, verbose_name=_('Type'))
    uploaded_file = models.FileField(upload_to='documents/', verbose_name=_('File'))

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
