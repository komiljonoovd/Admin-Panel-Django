from django.db import models


# Create your models here.
class ReportCategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, verbose_name='ID')
    createdon = models.DateTimeField(auto_now_add=True, db_column='CreatedOn', verbose_name='CreatedOn')
    modifiedon = models.DateTimeField(auto_now=True, db_column='ModifiedOn', verbose_name='ModifiedOn')
    createdby = models.CharField(db_column='CreatedBy', max_length=100, blank=False, verbose_name='CreatedBy')
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100, blank=True, null=True, verbose_name='ModifiedBy')
    isactive = models.BooleanField(db_column='IsActive', verbose_name='IsActive')
    name = models.CharField(db_column='Name', max_length=20,blank=False, verbose_name='Name')
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Report"."ReportCategory'  # Schema.Table
        verbose_name = 'Report Category'
        verbose_name_plural = 'Report Category'
