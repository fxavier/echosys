from django.contrib import admin
from core.models import Province, District, HealthFacility, DataSet, DataElement, OpenmrsURL, \
    DataSet, PeriodDescription, DataElementValue
from openmrs_dhis.models import OpenmrsOptimization
from openmrs.models import Paciente, Location, Inscricao, ConsultaClinica, \
    ConsultaApss, VisitaDomiciliaria, RelatorioVisita, ExameClinico


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
    list_display = ['id', 'province', 'openmrs_us',
                    'instance_name', 'uuid', 'url']


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


class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'nid', 'nome',
                    'distrito', 'localidade', 'bairro']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['location_id', 'codigo', 'name',
                    'description', 'state_province', 'parent_location']


admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(OpenmrsURL, OpenMRSURLAdmin)
admin.site.register(PeriodDescription)
admin.site.register(DataElementValue, DataElementValueAdmin)
admin.site.register(OpenmrsOptimization)
admin.site.register(Paciente, PatientAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Inscricao)
admin.site.register(ConsultaClinica)
admin.site.register(VisitaDomiciliaria)
admin.site.register(RelatorioVisita)
admin.site.register(ConsultaApss)
admin.site.register(ExameClinico)
