from django.contrib import admin
from django import forms

from drafts.models import DraftSupporter, DraftDrug, Draft


class DraftSupporterInline(admin.TabularInline):
    model = DraftSupporter

class DraftDrugInline(admin.TabularInline):
    model = DraftDrug
    autocomplete_fields = ['drug_brand', 'generic_drug']


@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Draft._meta.fields]
    fields = ['patient_case']
    readonly_fields = ['created_at']
    inlines = [DraftDrugInline, DraftSupporterInline]

    autocomplete_fields = ['patient_case']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        super().save_model(request, obj, form, change)
