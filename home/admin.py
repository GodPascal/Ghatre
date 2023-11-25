# Register your models here.

from django.contrib import admin
from home.models import PatientCase, Relative, OtherSupporter

class RelativeInline(admin.TabularInline):
    model = Relative

class OtherSupporterInline(admin.TabularInline):
    model = OtherSupporter

@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PatientCase._meta.fields]
    inlines = [
        RelativeInline,
        OtherSupporterInline
    ]