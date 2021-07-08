import graphene
from graphene_django import DjangoObjectType
from core.models import HealthFacility
from openmrs_viamo.models import Visit

        
class VisitType(DjangoObjectType): 
    class Meta:
        model = Visit
        
class Query(graphene.ObjectType):
    visits = graphene.List(VisitType)
    visit_province_date_range = graphene.List(VisitType, province=graphene.String(required=True), startDate=graphene.Date(required=True), endDate=graphene.Date(required=True))
  
    visit_date_range = graphene.List(VisitType, startDate=graphene.Date(required=True), endDate=graphene.Date(required=True))

    def resolve_visits(self, info):
        return Visit.objects.exclude(phone_number=None)
    
    def resolve_visit_province_date_range(self, info, province, startDate, endDate):
        return Visit.objects.filter(province=province, next_appointment_date__range=(startDate, endDate))
    
    def resolve_visit_date_range(self, info, startDate, endDate): 
        return Visit.objects.filter(next_appointment_date__range=(startDate, endDate))
    
    