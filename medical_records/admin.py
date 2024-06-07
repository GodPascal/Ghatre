from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from medical_records.models import RelativeDisease, MedicalRecord, PatientDisease, PatientDoctor, PatientDrugRecord, \
    DiseaseRecord
from utils.export_helpers import populate_pdf


class RelativeDiseaseInline(admin.TabularInline):
    model = RelativeDisease


class PatientDiseaseInline(admin.TabularInline):
    model = PatientDisease


class PatientDoctorInline(admin.TabularInline):
    model = PatientDoctor


class PatientDrugRecordInline(admin.TabularInline):
    model = PatientDrugRecord


@admin.register(DiseaseRecord)
class DiseaseRecordAdmin(admin.ModelAdmin):
    list_display = ['get_patient_name']
    inlines = [PatientDiseaseInline, PatientDoctorInline, PatientDrugRecordInline]

    @admin.display(description='Patient Name', ordering='patient__name')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Only set the created_by field if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.action(description=_('Export Pdf'))
def export_medical_record_as_pdf(modeladmin, request, queryset):
    context = {'medical_records': queryset}
    return populate_pdf(context, 'pdf-output-only-medical.html')


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['get_patient_name']
    inlines = [RelativeDiseaseInline]

    @admin.display(description='Patient Name', ordering='patient__name')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)

    actions = [export_medical_record_as_pdf]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Only set the created_by field if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
