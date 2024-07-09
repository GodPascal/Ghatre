from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from patients.models import Relative, OtherSupporter, Document, PatientCase
from utils.export_helpers import export_patient_as_pdf

import jdatetime


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
    list_display = ['pk', 'case_number', 'first_name', 'last_name', 'national_code', 'mobile_number']
    search_fields = ['first_name', 'last_name', 'national_code', 'mobile_number']
    list_filter = ['status']
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
        if not obj.case_number:
            current_year = jdatetime.datetime.now().year
            obj.case_number = '%s-%s' % (obj.id, current_year) 
        super().save_model(request, obj, form, change)
