# Register your models here.

from django.contrib import admin
from home.models import PatientCase, Relative, OtherSupporter, GenericDrug, DrugBrand, Draft, DraftSupporter, DraftDrug

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

class DraftSupporterInline(admin.TabularInline):
    model = DraftSupporter

class DraftDrugInline(admin.TabularInline):
    model = DraftDrug

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Draft._meta.fields]
    inlines = [DraftDrugInline, DraftSupporterInline]