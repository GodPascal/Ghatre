import jdatetime

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from medical_records.models import RelativeDisease, MedicalRecord, PatientDisease, \
    PatientDoctor, PatientDrugRecord, DiseaseRecord, PatientChart, TreatmentPlan, CurrentPatientState
from utils.export_helpers import populate_pdf


@admin.action(description=_('Export Pdf'))
def export_medical_record_as_pdf(modeladmin, request, queryset):
    context = {'medical_records': queryset}
    return populate_pdf(context, 'pdf-output-only-medical.html')


class RelativeDiseaseInline(admin.TabularInline):
    classes = ['collapse']
    model = RelativeDisease
    extra = 0


class PatientDiseaseInline(admin.TabularInline):
    model = PatientDisease
    classes = ['collapse']
    extra = 0


class PatientDrugRecordInline(admin.StackedInline):
    model = PatientDrugRecord
    classes = ['collapse']
    extra = 1
    raw_id_fields = ['generic_drug', 'drug_brand']
    fields = ['generic_drug', 'drug_brand', 'usage_start', 'usage_duration', 'usage_instruction',
              'prescription_number', 'unit_price', 'unit_price_display', 'patient_share',
              'price_difference', 'list_status', 'help_needed', 'intake_intervals', 'status']
    readonly_fields = ['unit_price_display']

    @admin.display(description=_('Cost Display'))
    def unit_price_display(self, instance):
        return f'{int(instance.unit_price or 0/10):,}'


class PatientDoctorInline(admin.TabularInline):
    model = PatientDoctor
    classes = ['collapse']
    extra = 0


class MedicalRecordInlineAdmin(admin.StackedInline):
    model = MedicalRecord
    classes = ['collapse']
    fields = ['patient_case', 'creator', 'created_at_display', 'diagnosis', 'diagnosis_tests', 'drug_history',
              'surgery_history', 'dietary_habits', 'movement_ability', 'routines_ability',
              'talking_and_swallowing', 'gatherings_attending', 'family_and_social',
              'height', 'weight', 'drugs_abuse', 'other_information', 'relative_disease']
    readonly_fields = ['creator', 'created_at_display', 'relative_disease']

    @admin.display(description=_('Patient Name'), ordering='patient_case__case_number')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)

    @admin.display(description=_('Relative Disease'))
    def relative_disease(self, obj):
        relative_part = ''
        for relative in obj.relativedisease_set.all():
            relative_part += '''
            <tr id="relativedisease_set-0" class="form-row has_original">
            <td class="original">
            <p>%s</p>
            <input id="id_relativedisease_set-0-id" name="relativedisease_set-0-id" type="hidden" value="1" /> <input id="id_relativedisease_set-0-medical_record" name="relativedisease_set-0-medical_record" type="hidden" value="1" /></td>
            <td class="field-relation">
            <p>%s</p>
            </td>
            <td class="field-disease_name">
            <p>%s</p>
            </td>
            <td class="field-infection_age">
            <p>%s</p>
            </td>
            <td class="field-current_health_status">
            <p>%s</p>
            </td>
            </tr>
            ''' % (relative.id, relative.relation, relative.disease_name, relative.infection_age, relative.current_health_status)

        return mark_safe('''
            <div id="relativedisease_set-group" class="js-inline-admin-formset inline-group" data-inline-type="tabular" data-inline-formset="{&quot;name&quot;: &quot;#relativedisease_set&quot;, &quot;options&quot;: {&quot;prefix&quot;: &quot;relativedisease_set&quot;, &quot;addText&quot;: &quot;\u0627\u0641\u0632\u0648\u062f\u0646 \u06cc\u06a9 \u0628\u06cc\u0645\u0627\u0631\u06cc \u0628\u0633\u062a\u06af\u0627\u0646 \u062f\u06cc\u06af\u0631&quot;, &quot;deleteText&quot;: &quot;\u062d\u0630\u0641&quot;}}">
            <div class="tabular inline-related last-related"><input id="id_relativedisease_set-TOTAL_FORMS" name="relativedisease_set-TOTAL_FORMS" type="hidden" value="2" /><input id="id_relativedisease_set-INITIAL_FORMS" name="relativedisease_set-INITIAL_FORMS" type="hidden" value="2" /><input id="id_relativedisease_set-MIN_NUM_FORMS" name="relativedisease_set-MIN_NUM_FORMS" type="hidden" value="0" /><input id="id_relativedisease_set-MAX_NUM_FORMS" name="relativedisease_set-MAX_NUM_FORMS" type="hidden" value="0" /><fieldset class="module collapse">
            <h2>سابقه بیماری بستگان</h2>
            <table>
            <thead>
            <tr>
            <th class="original">&nbsp;</th>
            <th class="column-relation">نسبت</th>
            <th class="column-disease_name">نام بیماری</th>
            <th class="column-infection_age">سن ابتلا</th>
            <th class="column-current_health_status">وضعیت سلامتی فعلی</th>
            </tr>
            </thead>
            <tbody>
            %s
            </tbody>
            </table>
            </fieldset></div>
            </div>
            ''' % (relative_part))

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)


class TreatmentPlanInline(admin.TabularInline):
    model = TreatmentPlan
    classes = ['collapse']
    fields = ['patient_case', 'pharmacist',
              'pharmacist_name', 'treatment_follow', 'status']
    readonly_fields = ['created_at_display', 'pharmacist_name']

    @admin.display(description=_('Pharmacist Name'))
    def pharmacist_name(self, instance):
        return f"{instance.pharmacist.first_name or ''}  {instance.pharmacist.last_name or ''}".strip() or instance.pharmacist.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)


class CurrentPatientStateInline(admin.StackedInline):
    model = CurrentPatientState
    classes = ['collapse']
    fields = ['patient_case', 'patient_state', 'current_symptom', 'main_treatment_process', 'other_description',
              'creator', 'created_at_display']
    readonly_fields = ['creator', 'created_at_display']

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    raw_id_fields = ['patient_case']
    list_display = ['get_patient_name']
    fields = ['patient_case', 'creator', 'created_at_display', 'gender', 'birthdate', 'diagnosis', 'diagnosis_tests', 'drug_history',
              'surgery_history', 'dietary_habits', 'movement_ability', 'routines_ability',
              'talking_and_swallowing', 'gatherings_attending', 'family_and_social',
              'height', 'weight', 'drugs_abuse', 'other_information']
    readonly_fields = ['creator', 'created_at_display', 'gender', 'birthdate']
    inlines = [RelativeDiseaseInline]

    @admin.display(description=_('Patient Name'), ordering='patient_case__case_number')
    def get_patient_name(self, obj):
        return '%s %s' % (obj.patient_case.first_name, obj.patient_case.last_name)

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Gender'))
    def gender(self, instance):
        return instance.patient_case.get_gender_display()

    @admin.display(description=_('Birthdate'))
    def birthdate(self, instance):
        return instance.patient_case.birthdate

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)

    actions = [export_medical_record_as_pdf]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(DiseaseRecord)
class DiseaseRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'case_number',
                    'first_name', 'last_name', 'phone_number']
    search_fields = ['patient__first_name',
                     'patient__last_name', 'patient__phone_number']
    fields = ['patient', 'phone_number', 'status', 'case_number']
    readonly_fields = ['patient', 'phone_number', 'status', 'case_number']
    inlines = [PatientDiseaseInline,
               PatientDrugRecordInline,
               PatientDoctorInline]


@admin.register(PatientChart)
class PatientChartAdmin(admin.ModelAdmin):
    inlines = [MedicalRecordInlineAdmin,
               PatientDiseaseInline,
               PatientDrugRecordInline,
               PatientDoctorInline,
               CurrentPatientStateInline,
               TreatmentPlanInline]
    list_display = ['id', 'case_number',
                    'first_name', 'last_name', 'phone_number']
    search_fields = ['patient__first_name', 'patient__last_name',
                     'patient__phone_number',  'case_number']
    fields = ['patient', 'phone_number', 'status', 'case_number']
    readonly_fields = ['patient', 'phone_number', 'status', 'case_number']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    fields = ['patient_case', 'pharmacist',
              'pharmacist_name', 'treatment_follow', 'status']
    readonly_fields = ['created_at_display', 'pharmacist_name']
    raw_id_fields = ['patient_case', 'pharmacist']
    search_fields = ['patient_case__patient__first_name',
                     'patient_case__patient__last_name']
    list_display = ['patient_case', 'created_at_display']

    @admin.display(description=_('Pharmacist Name'))
    def pharmacist_name(self, instance):
        return f"{instance.pharmacist.first_name or ''}  {instance.pharmacist.last_name or ''}".strip() or instance.pharmacist.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)


@admin.register(CurrentPatientState)
class CurrentPatientStateAdmin(admin.ModelAdmin):
    fields = ['patient_case', 'patient_state', 'current_symptom', 'main_treatment_process', 'other_description',
              'creator', 'created_at_display']
    readonly_fields = ['creator', 'created_at_display']
    raw_id_fields = ['patient_case']
    search_fields = ['patient_case__patient__first_name',
                     'patient_case__patient__last_name']
    list_display = ['patient_case', 'created_at_display']

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)
