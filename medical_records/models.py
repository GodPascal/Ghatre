from django.db import models
from django.utils.translation import gettext_lazy as _

from drugs.models import GenericDrug, DrugBrand
from home.models import BaseModel
from patients.models import PatientCase
from utils.consts import PATIENT_DRUG_LIST_STATUS_CHOICES, PATIENT_DRUG_STATUS_CHOICES, DISEASE_TYPE_CHOICES, \
    DISEASE_STATUS_CHOICES, PATIENT_DOCTOR_STATUS_CHOICES


class MedicalRecord(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    diagnosis = models.TextField(blank=True, verbose_name=_('Diagnosis'))
    diagnosis_tests = models.TextField(blank=True, verbose_name=_('Diagnosis Tests'))
    drug_history = models.TextField(blank=True, verbose_name=_('Drug History'))
    surgery_history = models.TextField(blank=True, verbose_name=_('Surgery History'))
    other_diseases = models.TextField(blank=True, verbose_name=_('Other Diseases'))
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
    treatment_facilities = models.CharField(blank=True, max_length=255, verbose_name=_('Treatment Facilities'))
    doctors_names = models.CharField(blank=True, max_length=255, verbose_name=_('Doctors Names'))

    class Meta:
        verbose_name = _('Medical Record')
        verbose_name_plural = _('Medical Records')


class DiseaseRecord(BaseModel):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    next_intake = models.CharField(max_length=100, blank=True, verbose_name=_('Next Intake'))
    prescription_cost = models.IntegerField(null=True, blank=True, verbose_name=_('Prescription Cost'))
    patient_claimed_cost = models.IntegerField(null=True, blank=True, verbose_name=_('Patient Claimed Cost'))
    pharmacy = models.CharField(max_length=255, blank=True, verbose_name=_('Pharmacy'))
    recipient = models.CharField(max_length=100, blank=True, verbose_name=_('Recipient'))
    description = models.TextField(blank=True, verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Disease Record')
        verbose_name_plural = _('Disease Records')


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


class PatientDrugRecord(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    disease_record = models.ForeignKey(DiseaseRecord, on_delete=models.CASCADE, verbose_name=_('Disease Record'))
    generic_drug = models.ForeignKey(GenericDrug, on_delete=models.CASCADE, verbose_name=_('Generic Drug'))
    drug_brand = models.ForeignKey(DrugBrand, on_delete=models.CASCADE, verbose_name=_('Drug Brand'))

    usage_start = models.CharField(max_length=30, verbose_name=_('Usage Start'))
    usage_duration = models.CharField(max_length=30, verbose_name=_('Usage Duration'))
    usage_instruction = models.CharField(max_length=30, verbose_name=_('Usage Instruction'))
    costs = models.IntegerField(null=True, blank=True, verbose_name=_('Costs'))
    costs_without_insurance = models.IntegerField(null=True, blank=True, verbose_name=_('Costs Without Insurance'))
    list_status = models.CharField(max_length=20, choices=PATIENT_DRUG_LIST_STATUS_CHOICES,
                                   verbose_name=_('List Status'))
    help_needed = models.BooleanField(verbose_name=_('Help Needed'))
    intake_intervals = models.CharField(max_length=100, verbose_name=_('Intake Intervals'))
    status = models.CharField(max_length=20, choices=PATIENT_DRUG_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Drug Record')
        verbose_name_plural = _('Patient Drug')


class PatientDisease(models.Model):
    disease_record = models.ForeignKey(DiseaseRecord, on_delete=models.CASCADE, verbose_name=_('Disease Record'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    disease_type = models.CharField(max_length=30, choices=DISEASE_TYPE_CHOICES, verbose_name=_('Disease Type'))
    disease_name = models.CharField(max_length=255, verbose_name=_('Disease Name'))
    diagnosis_year = models.IntegerField(verbose_name=_('Diagnosis Year'))
    status = models.CharField(max_length=20, choices=DISEASE_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Disease')
        verbose_name_plural = _('Patient Diseases')


class PatientDoctor(models.Model):
    disease_record = models.ForeignKey(DiseaseRecord, on_delete=models.CASCADE, verbose_name=_('Disease Record'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    doctor_name = models.CharField(blank=True, max_length=255, verbose_name=_('Doctor Name'))
    treatment_facilities = models.CharField(blank=True, max_length=255, verbose_name=_('Treatment Facilities'))
    status = models.CharField(max_length=20, choices=PATIENT_DOCTOR_STATUS_CHOICES, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Patient Doctor')
        verbose_name_plural = _('Patient Doctors')
