# Register your models here.

from django.contrib import admin
from home.models import PatientCase, Relative, OtherSupporter, Document, MedicalRecord

class RelativeInline(admin.TabularInline):
    model = Relative

class OtherSupporterInline(admin.TabularInline):
    model = OtherSupporter

class DocumentInline(admin.TabularInline):
    model = Document

@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PatientCase._meta.fields]
    inlines = [
        RelativeInline,
        OtherSupporterInline,
        DocumentInline
    ]


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['get_patient_name', 'disease_type', 'disease_name']
    @admin.display(description='Patient Name', ordering='patient__name')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)