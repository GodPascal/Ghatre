import jdatetime

from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from home.models import InputLog, InputLogHistory


class InputLogHistoryInline(admin.StackedInline):
    classes = ['collapse']
    model = InputLogHistory
    fields = ['status', 'last_action', 'description',
              'creator', 'created_at_display']
    readonly_fields = ['created_at_display', 'creator']
    extra = 0

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return instance.created_by.get_full_name() or instance.created_by.username

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class InputLogForm(forms.ModelForm):

    def clean_phone_number(self):
        if self.cleaned_data['phone_number'].isdigit():
            return self.cleaned_data['phone_number']

        raise forms.ValidationError(
            _('Number should only contain digits.'))


@admin.register(InputLog)
class InputLogAdmin(admin.ModelAdmin):
    form = InputLogForm

    list_display = ['entry_list_number',
                    'first_name', 'last_name', 'phone_number']
    search_fields = ['first_name', 'last_name', 'phone_number']
    fields = ['first_name', 'last_name', 'phone_number', 'disease_type',
              'disease_name', 'drugs_cost', 'drugs_cost_display', 'province_of_residence',
              'city_of_residence', 'referrer_name', 'age', 'has_social_insurance',
              'has_private_insurance', 'contact_location', 'service_date', 'creator',
              'contact_description', 'created_at_display']

    readonly_fields = ['creator', 'drugs_cost_display', 'created_at_display']
    inlines = [InputLogHistoryInline]

    @admin.display(description=_('Creator'))
    def creator(self, instance):
        return instance.created_by.get_full_name() or instance.created_by.username

    @admin.display(description=_('Cost Display'))
    def drugs_cost_display(self, instance):
        return f'{int(instance.drugs_cost or 0/10):,}'

    @admin.display(description=_('Created Date Display'))
    def created_at_display(self, instance):
        return jdatetime.datetime.fromgregorian(datetime=instance.created_at).strftime('%Y-%m-%d %H:%M')

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        for form in formset:
            model = type(form.instance)
            if not form.instance.pk and hasattr(model, 'created_by'):
                form.instance.created_by = request.user

        super().save_formset(request, form, formset, change)
