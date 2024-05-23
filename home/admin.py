# Register your models here.

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import *
from django.core import serializers
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.utils.translation import gettext_lazy as _




class RelativeInline(admin.TabularInline):
    model = Relative

class OtherSupporterInline(admin.TabularInline):
    model = OtherSupporter

class DocumentInline(admin.TabularInline):
    model = Document


class PatientCaseResource(resources.ModelResource):
    class Meta:
        model = PatientCase

@admin.action(description="Export patient data as json")
def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    
    # Initialize a list to store document URLs
    document_urls = []
    # Iterate through selected patients
    for patient in queryset:
        # Get associated PatientDocuments for each patient
        documents = patient.document_set.all()

        # Extract URLs from uploaded_file field
        for document in documents:
            document_urls.append(request.build_absolute_uri(document.uploaded_file.url))

    # Print or process the document URLs as needed
    print("Fetched document URLs:", document_urls)
    return response

@admin.action(description=_('Export Pdf'))
def export_patient_as_pdf(modeladmin, request, queryset):
    # Initialize a list to store document URLs
    document_urls = []
    # Iterate through selected patients
    for patient in queryset:
        # Get associated PatientDocuments for each patient
        documents = patient.document_set.all()
        # Extract URLs from uploaded_file field
        for document in documents:
            document_urls.append(request.build_absolute_uri(document.uploaded_file.url))
    
    context = {'patients': queryset, 'doc_urls': document_urls}
    
    return populate_pdf(context, 'pdf-output.html')

def populate_pdf(context, template_name):
    font_config = FontConfiguration()
    css = CSS(string='''
              @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap');
              @font-face {
                font-family: 'Vazirmatn';
              }
              body {
                font-family: Vazirmatn;
                font-size: 12px;}''', font_config=font_config)

    template = get_template(template_name)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    result = HTML(string=html).write_pdf(response, stylesheets=[css], font_config=font_config)
    response['Content-Disposition'] = 'attachment; filename="patient.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'
    return response

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
    

class RelativeDiseaseInline(admin.TabularInline):
    model = RelativeDisease

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

@admin.register(DrugBrand)
class DrugBrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrugBrand._meta.fields]
    inlines = []

@admin.register(GenericDrug)
class GenericDrugAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GenericDrug._meta.fields]
    inlines = []

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



class DraftSupporterInline(admin.TabularInline):
    model = DraftSupporter

class DraftDrugInline(admin.TabularInline):
    model = DraftDrug

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Draft._meta.fields]
    inlines = [DraftDrugInline, DraftSupporterInline]