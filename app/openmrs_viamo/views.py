from rest_framework import viewsets
from openmrs_viamo.serializers import VisitSerializer
from openmrs_viamo.models import Visit

class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = VisitSerializer
   # queryset = Appointment.objects.all()
    def get_queryset(self):
        queryset = Visit.objects.exclude(phone_number=None).all()
        province = self.request.query_params.get('province')
        startDate = self.request.query_params.get('startDate')
        endDate = self.request.query_params.get('endDate')
        if province is None and startDate is not None and endDate is not None:
            queryset = queryset.filter(next_appointment_date__range=(startDate, endDate))
        elif province is not None and startDate is not None and endDate is not None:
            queryset = queryset.filter(province=province, next_appointment_date__range=(startDate, endDate))
        return queryset