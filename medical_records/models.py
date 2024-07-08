from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from drugs.models import GenericDrug, DrugBrand
from home.models import BaseModel
from patients.models import PatientCase
from utils.consts import PATIENT_DRUG_LIST_STATUS_CHOICES, PATIENT_DRUG_STATUS_CHOICES, DISEASE_TYPE_CHOICES, \
    DISEASE_STATUS_CHOICES, PATIENT_DOCTOR_STATUS_CHOICES, INTERVAL_CHOICES


class MedicalRecord(BaseModel):
    patient_case = models.OneToOneField(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    diagnosis = models.TextField(blank=True, verbose_name=_('Diagnosis'))
    diagnosis_tests = models.TextField(blank=True, verbose_name=_('Diagnosis Tests'))
    drug_history = models.TextField(blank=True, verbose_name=_('Drug History'))
    surgery_history = models.TextField(blank=True, verbose_name=_('Surgery History'))
    dietary_habits = models.TextField(blank=True, verbose_name=_('Dietary Habits'))
    movement_ability = models.CharField(blank=True, max_length=255, verbose_name=_('Movement Ability'))
    routines_ability = models.CharField(blank=True, max_length=255, verbose_name=_('Routines Ability'))
    talking_and_swallowing = models.CharField(blank=True, max_length=255, verbose_name=_('Talking and Swallowing'))
    gatherings_attending = models.CharField(blank=True, max_length=255, verbose_name=_('Gatherings Attending'))
    family_and_social = models.CharField(blank=True, max_length=255, verbose_name=_('Family and Social'))

    height = models.FloatField(null=True, blank=True, verbose_name=_('Height'))
    weight = models.FloatField(null=True, blank=True, verbose_name=_('Weight'))

    drugs_abuse = models.CharField(blank=True, max_length=255, verbose_name=_('Drugs Abuse'))
    other_information = models.CharField(blank=True, max_length=255, verbose_name=_('Other Information'))
    doctors_names = models.CharField(blank=True, max_length=255, verbose_name=_('Doctors Names'))

    class Meta:
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')

    def __str__(self) -> str:
        return f'{self.pk}'


class RelativeDisease(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, verbose_name=_('Medical Record'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    relation = models.CharField(max_length=255, verbose_name=_('Relation'))
    disease_name = models.CharField(max_length=255, verbose_name=_('Disease Name'))
    infection_age = models.IntegerField(verbose_name=_('Infection Age'))
    current_health_status = models.CharField(max_length=255, verbose_name=_('Current Health Status'))

    class Meta:
        verbose_name = _('Relative Disease')
        verbose_name_plural = _('Relative Diseases')

    def __str__(self) -> str:
        return f'{self.pk}'


class PatientDisease(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    disease_type = models.CharField(max_length=30, choices=DISEASE_TYPE_CHOICES, verbose_name=_('Disease Type'))
    disease_name = models.CharField(max_length=255, verbose_name=_('Disease Name'))
    diagnosis_year = models.IntegerField(verbose_name=_('Diagnosis Year'))
    status = models.CharField(max_length=20, choices=DISEASE_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Disease')
        verbose_name_plural = _('Patient Diseases')

    def __str__(self) -> str:
        return f'{self.pk}'


class PatientDrugRecord(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    generic_drug = models.ForeignKey(GenericDrug, on_delete=models.CASCADE, verbose_name=_('Generic Drug'))
    drug_brand = models.ForeignKey(DrugBrand, on_delete=models.CASCADE, verbose_name=_('Drug Brand'))

    usage_start = jmodels.jDateField(verbose_name=_('Usage Start'))
    usage_duration = models.CharField(max_length=30, verbose_name=_('Usage Duration'))
    usage_instruction = models.TextField(verbose_name=_('Usage Instruction'))
    prescription_number = models.IntegerField(verbose_name=_('Prescription Number'))
    unit_price = models.IntegerField(verbose_name=_('Unit Price'))
    patient_share = models.IntegerField(verbose_name=_('Patient Share'))
    price_difference = models.IntegerField(verbose_name=_('Price Difference'))
    list_status = models.CharField(max_length=20, choices=PATIENT_DRUG_LIST_STATUS_CHOICES,
                                   verbose_name=_('List Status'))
    help_needed = models.BooleanField(verbose_name=_('Help Needed'))
    intake_intervals = models.CharField(max_length=20, choices=INTERVAL_CHOICES, verbose_name=_('Intake Intervals'))
    status = models.CharField(max_length=20, choices=PATIENT_DRUG_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Drug Record')
        verbose_name_plural = _('Patient Drug')
    
    def __str__(self) -> str:
        return f'{self.pk}'


class PatientDoctor(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    doctor_name = models.CharField(blank=True, max_length=255, verbose_name=_('Doctor Name'))
    center_name = models.CharField(blank=True, max_length=255, verbose_name=_('Center Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    status = models.CharField(max_length=20, choices=PATIENT_DOCTOR_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Doctor')
        verbose_name_plural = _('Patient Doctors')

    def __str__(self) -> str:
        return f'{self.pk}'

class DiseaseRecord(PatientCase):
    class Meta:
        proxy = True
        verbose_name = _('Disease Record')
        verbose_name_plural = _('Disease Records')


class PatientChart(PatientCase):
    class Meta:
        proxy = True
        verbose_name = _('Patient Chart')
        verbose_name_plural = _('Patient Charts')


class TreatmentPlan(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
   
    pharmacist = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Pharmacist'))
    treatment_follow = models.TextField(verbose_name=_('Treatment Follow'))
    status = models.CharField(max_length=20, choices=PATIENT_DRUG_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Treatment Plan')
        verbose_name_plural = _('Treatment Plans')

    def __str__(self) -> str:
        return f'{self.pk}'
    

class CurrentPatientState(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
  
    patient_state = models.TextField(verbose_name=_('Patient State'))
    current_symptom = models.TextField(verbose_name=_('Current Symptom'))
    main_treatment_process = models.TextField(verbose_name=_('Main Treatment Process'))
    other_description = models.TextField(verbose_name=_('Other Description'))

    class Meta:
        verbose_name = _('Current Patient State')
        verbose_name_plural = _('Current Patient States')

    def __str__(self) -> str:
        return f'{self.pk}'
