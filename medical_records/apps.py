from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MedicalRecordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medical_records'
    verbose_name = _('Medical Records Tab')
