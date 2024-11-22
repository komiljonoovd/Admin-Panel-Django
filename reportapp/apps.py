from django.apps import AppConfig


class ReportappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reportapp'
    verbose_name = 'Report'  # it will be changed on Admin Panel
