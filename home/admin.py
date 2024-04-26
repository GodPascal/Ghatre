# Register your models here.

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import PatientCase, Relative, OtherSupporter, Document, MedicalRecord
from django.core import serializers
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML



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

@admin.action(description="Export patient data as pdf")
def export_as_pdf(modeladmin, request, queryset):
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
    
    
    template = get_template('pdf-output.html')
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    result = HTML(string=html).write_pdf(response)
    response['Content-Disposition'] = 'attachment; filename="patient.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'
    return response

@admin.register(PatientCase)
class PatientCaseAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in PatientCase._meta.fields]
    inlines = [
        RelativeInline,
        OtherSupporterInline,
        DocumentInline
    ]
    resource_classes = [PatientCaseResource]
    actions = [export_as_json, export_as_pdf]
    




@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['get_patient_name', 'disease_type', 'disease_name']
    @admin.display(description='Patient Name', ordering='patient__name')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)