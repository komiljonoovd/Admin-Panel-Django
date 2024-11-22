from django.contrib import admin
from .models import ReportCategory


# Register your models here.

@admin.register(ReportCategory)
class ReportCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdon', 'modifiedon', 'createdby', 'modifiedby', 'description', 'isactive')
    list_display_links = ('id', 'name')
    list_filter = ('createdon', 'modifiedon', 'isactive')
    search_fields = ('id', 'name', 'createdby', 'modifiedby', 'description')
    ordering = ['id']
    list_per_page = 30
