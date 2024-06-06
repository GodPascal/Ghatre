from django.db import models
from django.utils.translation import gettext_lazy as _


class GenericDrug(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Generic Drug')
        verbose_name_plural = _('Generic Drugs')


class DrugBrand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name=_('Brand Name'))
    country = models.CharField(max_length=30, verbose_name=_('Country'))
    address = models.CharField(max_length=255, verbose_name=_('Address'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Created At'))
    modified_at = models.DateField(auto_now=True, verbose_name=_('Modified At'))

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = _('Drug Brand')
        verbose_name_plural = _('Drug Brands')
