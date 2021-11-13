from django.contrib import admin
from openmrs_viamo.models import Visit


class VisitAdmin(admin.ModelAdmin):
    ordering = ['patient_name', 'next_appointment_date']
    list_display = ['patient_name', 'appointment_date', 'next_appointment_date', 'health_facility']

admin.site.register(Visit, VisitAdmin)