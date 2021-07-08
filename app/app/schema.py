import graphene
import openmrs_viamo.schema
import openmrs_dhis.schema

class Query(openmrs_viamo.schema.Query, openmrs_dhis.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)