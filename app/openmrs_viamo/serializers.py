from rest_framework import serializers
from openmrs_viamo.models import Visit

        
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = (
            'id',
            'type_visit',
            'province',
            'district',
            'health_facility',
            'patient_id', 
            'patient_identifier',
            'age',
            'gender',
            'phone_number',
            'appointment_date',
            'next_appointment_date',
            'community',
            'pregnant',
            'brestfeeding',
            'tb'
        )
        read_only_fields = ('id',)