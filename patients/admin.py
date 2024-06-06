from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from patients.models import Relative, OtherSupporter, Document, PatientCase
from utils.export_helpers import export_patient_as_pdf


class RelativeInline(admin.TabularInline):
    model = Relative


class OtherSupporterInline(admin.TabularInline):
    model = OtherSupporter


class DocumentInline(admin.TabularInline):
    model = Document


class PatientCaseResource(resources.ModelResource):
    class Meta:
        model = PatientCase


@admin.register(PatientCase)
class PatientCaseAdmin(ImportExportModelAdmin):
    list_display = ['case_number', 'first_name', 'last_name']
    inlines = [
        RelativeInline,
        OtherSupporterInline,
        DocumentInline
    ]

    resource_classes = [PatientCaseResource]
    actions = [export_patient_as_pdf]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Only set the created_by field if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
