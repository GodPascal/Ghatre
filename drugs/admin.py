from django.contrib import admin

from drugs.models import DrugBrand, GenericDrug


@admin.register(DrugBrand)
class DrugBrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrugBrand._meta.fields]
    search_fields = ['brand_name']
    inlines = []


@admin.register(GenericDrug)
class GenericDrugAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GenericDrug._meta.fields]
    search_fields = ['name']
    inlines = []
