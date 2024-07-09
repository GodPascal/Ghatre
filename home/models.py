from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

from utils.consts import DISEASE_TYPE_CHOICES, PROVINCES_OF_IRAN_CHOICES, INPUT_LOG_STATUS_CHOICES, DESCRIPTION_OF_THE_LAST_ACTION, INPUT_DRAFT_STATUS_CHOICES


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    class Meta:
        abstract = True  # This ensures that this model won't create a database table

    def save_model(self, request, obj, form, change):
        if not self.id:
            # Only set the created_by field if the object is being created
            self.created_by = request.user
        super().save_model(request, obj, form, change)


class InputLog(BaseModel):
    created_at = models.DateField(
        auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(
        auto_now=True, verbose_name=_('Modified At'))

    first_name = models.CharField(
        max_length=255, verbose_name=_('First Name'), blank=False)
    last_name = models.CharField(
        max_length=255, verbose_name=_('Last Name'), blank=False)
    phone_number = models.CharField(
        max_length=20, blank=True, verbose_name=_('Phone Number'))
    contact_location = models.CharField(
        max_length=100, verbose_name=_('Contact Location'), blank=False)
    disease_type = models.CharField(
        max_length=30, choices=DISEASE_TYPE_CHOICES, verbose_name=_('Disease Type'), blank=False)
    disease_name = models.CharField(
        max_length=255, verbose_name=_('Disease Name'), blank=False)
    drugs_cost = models.IntegerField(verbose_name=_('Drugs Cost'), blank=False)
    treatment_program = models.CharField(
        max_length=100, blank=True, verbose_name=_('Treatment Program'))
    province_of_residence = models.CharField(
        max_length=30, choices=PROVINCES_OF_IRAN_CHOICES, blank=True, verbose_name=_('Province of Residence'))
    city_of_residence = models.CharField(
        max_length=255, blank=True, verbose_name=_('City of Residence'))
    referrer_name = models.CharField(
        max_length=255, blank=True, verbose_name=_('Referrer Name'))
    birthdate = jmodels.jDateField(
        null=True, verbose_name=_('Birthdate'), blank=False)
    contact_description = models.TextField(
        verbose_name=_('Contact Description'), blank=False)
    has_social_insurance = models.BooleanField(
        verbose_name=_('Has Social Insurance'))
    has_private_insurance = models.BooleanField(
        verbose_name=_('Has Private Insurance'))

    status = models.CharField(
        max_length=30, choices=INPUT_LOG_STATUS_CHOICES, verbose_name=_('Status'))
    last_action = models.CharField(
        max_length=255, choices=DESCRIPTION_OF_THE_LAST_ACTION, verbose_name=_('Last Action'), blank=False)
    last_action_date = jmodels.jDateField(
        null=True, verbose_name=_('Last Action Date'), blank=False)
    description = models.TextField(blank=True, verbose_name=_('Description'))
    input_draft_status = models.CharField(
        max_length=30, choices=INPUT_DRAFT_STATUS_CHOICES, verbose_name=_('Input Draft Status'))

    class Meta:
        verbose_name = _('Input Log')
        verbose_name_plural = _('Input Logs')

    def __str__(self) -> str:
        return '%s       %s' % (self.first_name, self.last_name)
