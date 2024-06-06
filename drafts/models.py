from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from drugs.models import GenericDrug, DrugBrand
from patients.models import PatientCase, OtherSupporter
from utils.consts import DRAFT_TYPE_CHOICES, DRAFT_STATUS_CHOICES, SUPPLIER_TYPE_CHOICES


class Draft(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Creator'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, verbose_name=_('Patient Case'))
    draft_type = models.CharField(max_length=10, choices=DRAFT_TYPE_CHOICES, verbose_name=_('Draft Type'))
    status = models.CharField(max_length=30, choices=DRAFT_STATUS_CHOICES, verbose_name=_('Status'))
    draft_create_date = models.DateField(verbose_name=_('Draft Create Date'))
    draft_receive_date = models.DateField(verbose_name=_('Draft Receive Date'))
    drug_receive_date = models.DateField(verbose_name=_('Drug Receive Date'))
    invoice_create_date = models.DateField(verbose_name=_('Invoice Create Date'))
    payment_date = models.DateField(verbose_name=_('Payment Date'))
    invoice_amount = models.PositiveIntegerField(verbose_name=_('Invoice Amount'))
    cash_draft_amount = models.PositiveIntegerField(verbose_name=_('Cash Draft Amount'))
    drug_draft_amount = models.PositiveIntegerField(verbose_name=_('Drug Draft Amount'))
    patient_amount = models.PositiveIntegerField(verbose_name=_('Patient Amount'))
    insurance_amount = models.PositiveIntegerField(verbose_name=_('Insurance Amount'))
    supplier_type = models.CharField(max_length=10, choices=SUPPLIER_TYPE_CHOICES, verbose_name=_('Supplier Type'))
    supplier_name = models.CharField(max_length=255, verbose_name=_('Supplier Name'), default=None)

    class Meta:
        verbose_name = _('Draft')
        verbose_name_plural = _('Drafts')


class DraftSupporter(models.Model):
    draft = models.ForeignKey(Draft, on_delete=models.CASCADE, verbose_name=_('Draft'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    supporter = models.ForeignKey(OtherSupporter, on_delete=models.CASCADE, verbose_name=_('Supporter'))
    support_amount = models.PositiveIntegerField(verbose_name=_('Support Amount'))

    class Meta:
        verbose_name = _('Draft Supporter')
        verbose_name_plural = _('Draft Supporters')


class DraftDrug(models.Model):
    draft = models.ForeignKey(Draft, on_delete=models.CASCADE, verbose_name=_('Draft'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))
    generic_drug = models.ForeignKey(GenericDrug, on_delete=models.CASCADE, verbose_name=_('Generic Drug'))
    drug_brand = models.ForeignKey(DrugBrand, on_delete=models.CASCADE, verbose_name=_('Drug Brand'), default=None)
    count = models.PositiveIntegerField(verbose_name=_('Count'))

    class Meta:
        verbose_name = _('Draft Drug')
        verbose_name_plural = _('Draft Drugs')
