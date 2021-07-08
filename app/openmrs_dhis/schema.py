import graphene
from graphene_django.types import DjangoObjectType
from core.models import Province, District, HealthFacility, DataSet, DataElement, OpenmrsURL


class ProvinceType(DjangoObjectType):
    class Meta:
        model = Province
        
class DistrictType(DjangoObjectType):
    class Meta:
        model = District

class HealthFacilityType(DjangoObjectType): 
    class Meta:
        model = HealthFacility
        
class DataSetType(DjangoObjectType): 
    class Meta:
        model = DataSet
        
class DataElementType(DjangoObjectType):
    class Meta:
        model = DataElement
        
class OpenmrsURLType(DjangoObjectType):
    class Meta:
        model = OpenmrsURL
        
class Query(graphene.ObjectType):
    provinces = graphene.List(ProvinceType)
    districts = graphene.List(DistrictType, province_id=graphene.Int())
    health_facilities = graphene.List(HealthFacilityType, district_id=graphene.Int())
  

    def resolve_provinces(self, info):
        return Province.objects.all()

    def resolve_districts(self, info, province_id):
        return District.objects.filter(province_id=province_id)
    
    def resolve_health_facilities(self, info, district_id): 
        return HealthFacility.objects.filter(district_id=district_id)