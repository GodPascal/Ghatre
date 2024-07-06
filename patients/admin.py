import jdatetime

from import_export.admin import ImportExportModelAdmin
from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from patients.models import Relative, OtherSupporter, Document, SupportProgram, \
    PatientCase, LivelihoodAssessment, ApplicationSupport, PatientHelperHistory
from utils.export_helpers import export_patient_as_pdf


class DocumentInline(admin.TabularInline):
    classes = ['collapse']
    model = Document
    extra = 1


class RelativeInline(admin.StackedInline):
    classes = ['collapse']
    model = Relative
    extra = 1


class LivelihoodAssessmentInline(admin.StackedInline):
    classes = ['collapse']
    model = LivelihoodAssessment
    fields = ['created_at_display', 'housing_status', 'deposit_amount', 'rent_amount', 'has_job',
              'job_description', 'monthly_income', 'other_monthly_income', 'subsidy',
              'family_monthly_expenses', 'amount_of_installment_or_debt', 'repayment_due_date',
              'income_expenses_description', 'patient_problem', 'drugs_cost', 'recipient', 'helper_comment',
              'helper_assessment', 'creator'
              ]
    readonly_fields = ['created_at_display', 'creator', 'drugs_cost']
    extra = 1

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)

    @admin.display(description=_('Drugs Cost'))
    def drugs_cost(self, instance):
        return f'{int(instance.patient_case.patient.drugs_cost):,}'


class ApplicationSupportInline(admin.StackedInline):
    classes = ['collapse']
    model = ApplicationSupport
    fields = ['multiple_receive', 'first_intake_date', 'prescription_cost', 'help_intervals',
              'supplier_pharmacy', 'description']
    readonly_fields = []
    extra = 1


class OtherSupporterInline(admin.TabularInline):
    classes = ['collapse']
    model = OtherSupporter
    extra = 1


class PatientHelperHistoryInline(admin.TabularInline):
    classes = ['collapse']
    model = PatientHelperHistory
    fields = ['patient_description', 'creator', 'created_at_display']
    readonly_fields = ['creator', 'created_at_display']
    extra = 1

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)


class SupportProgramForm(forms.ModelForm):
    def clean_percentage(self):
        if 0 <= self.cleaned_data['percentage'] <= 100:
            return self.cleaned_data['percentage']

        raise forms.ValidationError(
            _('Please enter a correct value for percentage.'))


class SupportProgramInline(admin.StackedInline):
    classes = ['collapse']
    model = SupportProgram
    form = SupportProgramForm
    fields = ['percentage', 'amount', 'intervals', 'count',
              'end_date', 'support_program', 'program_type', 'service_pharmacy',
              'drug_delivery_type', 'status']
    extra = 1


class PatientCaseForm(forms.ModelForm):
    def clean_home_number(self):
        if self.cleaned_data['home_number'].isdigit():
            return self.cleaned_data['home_number']

        raise forms.ValidationError(
            _('Number should only contain digits.'))

    def clean_representor_phone(self):
        if self.cleaned_data['representor_phone'].isdigit():
            return self.cleaned_data['representor_phone']

        raise forms.ValidationError(
            _('Number should only contain digits.'))


@admin.register(PatientCase)
class PatientCaseAdmin(ImportExportModelAdmin):
    form = PatientCaseForm
    list_display = ['pk', 'case_number', 'first_name',
                    'last_name', 'national_code', 'phone_number']
    search_fields = ['first_name', 'last_name',
                     'national_code', 'phone_number']
    fields = ['patient', 'status', 'case_number', 'service_date', 'case_completion_date', 'creator', 'referrer_name',
              'father_name', 'gender', 'birthdate', 'national_code', 'nationality', 'guardian_status', 'first_guardian_name',
              'first_guardian_national_code', 'first_guardian_relation', 'second_guardian_name', 'second_guardian_national_code',
              'second_guardian_relation', 'has_social_insurance', 'social_insurance_type', 'social_insurance_description',
              'has_private_insurance', 'private_insurance_name', 'private_insurance_description', 'educational_status',
              'marital_status', 'marital_status_description', 'province_of_residence', 'city_of_residence', 'address',
              'phone_number', 'home_number', 'representor', 'representor_relation', 'representor_phone', 'other_information',
              'description', 'created_at_display'
              ]

    readonly_fields = ['creator', 'created_at_display', 'phone_number', 'service_date', 'referrer_name', 'case_number',
                       'has_social_insurance', 'has_private_insurance', 'province_of_residence', 'city_of_residence', ]
    list_filter = ['status']
    inlines = [
        DocumentInline,
        RelativeInline,
        LivelihoodAssessmentInline,
        ApplicationSupportInline,
        OtherSupporterInline,
        PatientHelperHistoryInline,
        SupportProgramInline,
    ]

    actions = [export_patient_as_pdf]

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return f"{instance.created_by.first_name or ''}  {instance.created_by.last_name or ''}".strip() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at)

    @admin.display(description=_('Service Date'))
    def service_date(self, instance):
        return instance.patient.service_date

    @admin.display(description=_('Referrer Name'))
    def referrer_name(self, instance):
        return instance.patient.referrer_name

    @admin.display(description=_('Has Social Insurance'))
    def has_social_insurance(self, instance):
        return _('Yes') if instance.patient.has_social_insurance else _('No')

    @admin.display(description=_('Has Private Insurance'))
    def has_private_insurance(self, instance):
        return _('Yes') if instance.patient.has_private_insurance else _('No')

    @admin.display(description=_('Province of Residence'))
    def province_of_residence(self, instance):
        return instance.patient.get_province_of_residence_display()

    @admin.display(description=_('City of Residence'))
    def city_of_residence(self, instance):
        return instance.patient.city_of_residence

    @admin.display(description=_('Phone Number'))
    def phone_number(self, instance):
        return instance.patient.phone_number

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            current_year = jdatetime.datetime.now().year
            obj.case_number = '%s-%s' % (obj.id, current_year)

        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        for form in formset:
            model = type(form.instance)
            if not form.instance.pk and hasattr(model, 'created_by'):
                form.instance.created_by = request.user

        super().save_formset(request, form, formset, change)
