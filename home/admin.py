# Register your models here.

from django.contrib import admin
from home.models import PatientCase, Relative, OtherSupporter, GenericDrug, DrugBrand

class RelativeInline(admin.TabularInline):
    model = Relative

class OtherSupporterInline(admin.TabularInline):
    model = OtherSupporter

@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PatientCase._meta.fields]
    inlines = [
        RelativeInline,
        OtherSupporterInline
    ]

@admin.register(DrugBrand)
class DrugBrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrugBrand._meta.fields]
    inlines = []

@admin.register(GenericDrug)
class GenericDrugAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GenericDrug._meta.fields]
    inlines = []