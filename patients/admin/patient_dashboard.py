import jdatetime

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from patients.models import PatientDashboard, PatientHelperHistory, SupportProgram
from medical_records.models import PatientDisease, CurrentPatientState, PatientDrugRecord, \
    PatientDoctor, MedicalRecord, TreatmentPlan


class PharmacistInline(admin.TabularInline):
    model = TreatmentPlan
    classes = ['collapse']
    fields = ['pharmacist_name', 'pharmacist_email']
    readonly_fields = ['pharmacist_name', 'pharmacist_email']
    verbose_name = _('Pharmacist')
    verbose_name_plural = _('Pharmacists')

    @admin.display(description=_('Pharmacist Name'))
    def pharmacist_name(self, instance):
        return f"{instance.pharmacist.first_name or ''}  {instance.pharmacist.last_name or ''}".strip() or instance.pharmacist.username

    @admin.display(description=_('Pharmacist Email'))
    def pharmacist_email(self, instance):
        return instance.pharmacist.email


class PatientDiseaseInline(admin.TabularInline):
    model = PatientDisease
    classes = ['collapse']


class CurrentPatientStateInline(admin.StackedInline):
    model = CurrentPatientState
    classes = ['collapse']
    fields = ['patient_case', 'patient_state', 'current_symptom', 'main_treatment_process', 'other_description',
              'creator', 'created_at_display']
    readonly_fields = ['creator', 'created_at_display']

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return instance.created_by.get_full_name() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        last_record = qs.last()
        return qs.filter(id__in=[last_record.pk] if last_record else [])


class PatientHelperHistoryInline(admin.TabularInline):
    classes = ['collapse']
    model = PatientHelperHistory
    fields = ['patient_description', 'creator', 'created_at_display']
    readonly_fields = ['creator', 'created_at_display']

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return instance.created_by.get_full_name() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        last_record = qs.last()
        return qs.filter(id__in=[last_record.pk] if last_record else [])


class PatientDrugRecordInline(admin.StackedInline):
    model = PatientDrugRecord
    classes = ['collapse']
    fields = ['generic_drug', 'drug_brand', 'usage_start', 'usage_duration', 'usage_instruction',
              'prescription_number', 'unit_price', 'unit_price_display', 'patient_share',
              'price_difference', 'list_status', 'help_needed', 'intake_intervals', 'status']
    readonly_fields = ['unit_price_display']

    @admin.display(description=_('Cost Display'))
    def unit_price_display(self, instance):
        return f'{int(instance.unit_price or 0/10):,}'


class SupportProgramInline(admin.StackedInline):
    classes = ['collapse']
    model = SupportProgram
    fields = ['total_other_support', 'percentage', 'amount', 'intervals', 'count',
              'end_date', 'support_program', 'program_type', 'patient_final_payment',
              'service_pharmacy', 'drug_delivery_type', 'status']
    readonly_fields = ['total_other_support', 'patient_final_payment']

    @admin.display(description=_('Patient Final Payment'))
    def patient_final_payment(self, instance):
        return instance.patient_case.patient_final_payment - instance.total_other_support


class PatientDoctorInline(admin.TabularInline):
    model = PatientDoctor
    classes = ['collapse']


@admin.register(PatientDashboard)
class PatientDashboardAdmin(ImportExportModelAdmin):
    list_display = ['case_number', 'first_name',
                    'last_name', 'national_code']
    search_fields = ['patient__first_name', 'patient__last_name',
                     'national_code', 'patient__phone_number', 'case_number']
    fieldsets = (
        ((_('Patient Case'), {'fields': ('patient', 'case_number', 'status', 'birthdate', 'national_code',  'first_guardian_name',
                                         'first_guardian_national_code', 'first_guardian_relation', 'representor', 'representor_relation',
                                         'representor_phone', 'service_date', 'has_social_insurance', 'has_private_insurance',
                                         'province_of_residence'
                                         ), 'classes': ['collapse'], }),
            (_('Helper'), {'fields': ('helper_name',
             'helper_email'), 'classes': ['collapse']}),
            (_('Medical Record Expert'), {'fields': ('medical_record_expert_name', 'medical_record_expert_email'), 'classes': ['collapse']}))
    )
    inlines = [
        PharmacistInline,
        PatientHelperHistoryInline,
        PatientDiseaseInline,
        CurrentPatientStateInline,
        PatientDrugRecordInline,
        SupportProgramInline,
        PatientDoctorInline,
    ]
    readonly_fields = ['service_date', 'case_number', 'has_social_insurance',
                       'has_private_insurance', 'province_of_residence']
    list_filter = ['status']
    raw_id_fields = ['patient']

    @admin.display(description=_('Service Date'))
    def service_date(self, instance):
        return instance.patient.service_date

    @admin.display(description=_('Has Social Insurance'))
    def has_social_insurance(self, instance):
        return _('Yes') if instance.patient.has_social_insurance else _('No')

    @admin.display(description=_('Has Private Insurance'))
    def has_private_insurance(self, instance):
        return _('Yes') if instance.patient.has_private_insurance else _('No')

    @admin.display(description=_('Province of Residence'))
    def province_of_residence(self, instance):
        return instance.patient.get_province_of_residence_display()

    @admin.display(description=_('Helper Name'))
    def helper_name(self, instance):
        return f'{instance.patient.created_by.first_name} {instance.patient.created_by.last_name}'

    @admin.display(description=_('Helper Email'))
    def helper_email(self, instance):
        return instance.patient.created_by.email

    @admin.display(description=_('Medical Record Expert Name'))
    def medical_record_expert_name(self, instance):
        expert = MedicalRecord.objects.filter(patient_case=instance
                                              ).values_list('created_by__first_name', 'created_by__last_name')
        return f'{expert[0][0]} {expert[0][1]}' if list(expert) else ''

    @admin.display(description=_('Medical Record Expert Email'))
    def medical_record_expert_email(self, instance):
        expert = MedicalRecord.objects.filter(patient_case=instance
                                              ).values_list('created_by__email', flat=True)
        return expert[0] if list(expert) else ''

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
