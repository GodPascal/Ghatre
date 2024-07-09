from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jModels

from drugs.models import GenericDrug, DrugBrand
from patients.models import PatientCase, OtherSupporter
from utils.consts import DRAFT_TYPE_CHOICES, DRAFT_STATUS_CHOICES, DRAFT_RECEIVE_STATUS_CHOICES, DRAFT_RECEIVER_CHOICES, SUPPORT_TYPE_CHOICES, DRAFT_CAUSED_CHOICES, DRAFT_STATUS_CHOICES


class Draft(models.Model):
    # data modify information
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Creator'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    # patient case information
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))

    # statuses
    receive_status=models.CharField(max_length=20,choices=DRAFT_RECEIVE_STATUS_CHOICES, default='pending', verbose_name=_('Receive Status'))
    receive_description=models.TextField(default=None, blank=True, verbose_name=_('Receive Description'))
    status=models.CharField(max_length=20,choices=DRAFT_STATUS_CHOICES, default=None, verbose_name=_('Status'))

    # prices
    total_amount=models.FloatField(verbose_name=_('Total Amount'))
    patient_amount=models.FloatField(verbose_name=_('Patient Amount'))
    insurance_amount=models.FloatField(verbose_name=_('Insurance Amount'))
    cash_amount=models.FloatField(verbose_name=_('Cash Amount'))
    medicine_amount=models.FloatField(verbose_name=_('Medicine Amount'))
    franchise=models.FloatField(verbose_name=_('Franchise'))


    # draft information
    draft_type = models.CharField(max_length=10, choices=DRAFT_TYPE_CHOICES, verbose_name=_('Draft Type'))
    draft_receiver = models.CharField(max_length=30,choices=DRAFT_RECEIVER_CHOICES, verbose_name=_('Draft Receiver'))
    receiving_center=models.CharField(max_length=200, verbose_name=_('Receiving Center'))
    draft_caused = models.CharField(max_length=30, choices=DRAFT_CAUSED_CHOICES, verbose_name=_('Draft Caused'))
    support_type = models.CharField(max_length=10, choices=SUPPORT_TYPE_CHOICES, verbose_name=_('Support Type'))
    description=models.TextField(default=None, blank=True, verbose_name=_('Description'))
    modify_description=models.TextField(default=None, blank=True, verbose_name=_('Modify Description'))

    # invoice information
    invoice_create_date = models.DateField(verbose_name=_('Invoice Create Date'))
    invoice_amount = models.PositiveIntegerField(verbose_name=_('Invoice Amount'))

    next_visit=jModels.jDateField(default=None, verbose_name=_('Next Visit'))
    status = models.CharField(max_length=30, choices=DRAFT_STATUS_CHOICES, verbose_name=_('Status'))
    draft_receive_date = models.DateField(verbose_name=_('Draft Receive Date'))
    drug_receive_date = models.DateField(verbose_name=_('Drug Receive Date'))
    payment_date = models.DateField(verbose_name=_('Payment Date'))

    class Meta:
        verbose_name = _('Draft')
        verbose_name_plural = _('Drafts')


class DraftSupporter(models.Model):
    draft=models.ForeignKey(Draft, on_delete=models.CASCADE, verbose_name=_('Draft'))

    created_at=models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at=models.DateField(auto_now=True, verbose_name=_('Modified At'))
    supporter=models.ForeignKey(OtherSupporter, on_delete=models.CASCADE, verbose_name=_('Supporter'))
    support_amount=models.PositiveIntegerField(verbose_name=_('Support Amount'))

    class Meta:
        verbose_name = _('Draft Supporter')
        verbose_name_plural = _('Draft Supporters')


class DraftDrug(models.Model):
    created_at=models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at=models.DateField(auto_now=True, verbose_name=_('Modified At'))

    draft=models.ForeignKey(Draft, on_delete=models.CASCADE, verbose_name=_('Draft'))
    generic_drug=models.ForeignKey(GenericDrug, on_delete=models.CASCADE, verbose_name=_('Generic Drug'))
    drug_brand=models.ForeignKey(DrugBrand, on_delete=models.CASCADE, verbose_name=_('Drug Brand'), default=None)
    dose=models.CharField(max_length=256, verbose_name=_('Dose'))
    start_date=jModels.jDateField(verbose_name=_('Start Taking Date'))
    duration=models.PositiveIntegerField(verbose_name=_('Duration(Day)'))
    count=models.PositiveIntegerField(verbose_name="Count")
    unit_price=models.PositiveIntegerField(verbose_name="Unit Price")

    class Meta:
        verbose_name = _('Draft Drug')
        verbose_name_plural = _('Draft Drugs')
