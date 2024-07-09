import jdatetime

from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from drugs.models import DrugBrand, GenericDrug


class DrugBrandForm(forms.ModelForm):
    def clean_phone(self):
        if self.cleaned_data['phone'].isdigit():
            return self.cleaned_data['phone']

        raise forms.ValidationError(
            _('Number should only contain digits.'))


@admin.register(DrugBrand)
class DrugBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand_name',
                    'country', 'phone', 'created_at_display']
    search_fields = ['brand_name']

    readonly_fields = ['created_at_display']
    form = DrugBrandForm

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')


@admin.register(GenericDrug)
class GenericDrugAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at_display']
    search_fields = ['name']
    readonly_fields = ['created_at_display']

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')
