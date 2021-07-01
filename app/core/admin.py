from django.contrib import admin
from core.models import Province, District, HealthFacility, DataSet, DataElement, OpenmrsURL, \
                        DataSet, PeriodDescription, DataElementValue

class DataElementAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = [
        'id',
        'name',
        'openmrs'
        ]
    
class DataSetAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name']
    
class ProvinceAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name']
    
class DistrictAdmin(admin.ModelAdmin):
    ordering = ['province']
    list_display = ['id', 'name', 'province']
    
class HealthFacilityAdmin(admin.ModelAdmin):
    ordering = ['district']
    list_display = ['id', 'name', 'district']

    
class OpenMRSURLAdmin(admin.ModelAdmin):
    ordering = ['province']
    list_display = ['province', 'instance_name', 'uuid', 'url']


class PeriodDescriptionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'ano',
        'mes',
        'period_ref',
        'period'
    ]
    
class DataElementValueAdmin(admin.ModelAdmin):
    ordering = ['period']
    list_display = [
        'period',
        'value',
        'dataElement',
        'healthFacility',
        'synced'
    ]

admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(OpenmrsURL, OpenMRSURLAdmin)
admin.site.register(PeriodDescription)
admin.site.register(DataElementValue, DataElementValueAdmin)