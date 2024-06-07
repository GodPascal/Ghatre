from django.contrib import admin

from drafts.models import DraftSupporter, DraftDrug, Draft


class DraftSupporterInline(admin.TabularInline):
    model = DraftSupporter


class DraftDrugInline(admin.TabularInline):
    model = DraftDrug


@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Draft._meta.fields]
    inlines = [DraftDrugInline, DraftSupporterInline]
