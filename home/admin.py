from django.contrib import admin
from home.models import *


@admin.register(InputLog)
class InputLogAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number']

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Only set the created_by field if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
