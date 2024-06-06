from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.utils.translation import gettext_lazy as _


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
