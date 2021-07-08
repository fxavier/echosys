from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs_dhis.services.metadata_import import ImportMetadata
from openmrs_dhis.services.art_optimization import get_openmrs_optimization


@shared_task
def load_orgunits():
    orgUnits = ImportMetadata()
    orgUnits.import_org_units('orgUnits_dhis.csv')
                
@shared_task
def load_dataElements():
    dataElements = ImportMetadata()
    dataElements.import_data_elements('dataElements.csv')
    
@shared_task
def load_openmrs_urls(): 
    urls = ImportMetadata()
    urls.import_openmrs_urls('openmrs_urls.csv')
    
@shared_task
def get_openmrs_optimization():
    get_openmrs_optimization()
    
                
# @shared_task
# def get_ped_optimization():
#     art_optimization = ARTOptimization()
#     art_optimization.get_openmrs_optimization() 
    
# @shared_task
# def post_ped_art_optimization():
#     art_optimization = ARTOptimization()
#     art_optimization.post_ped_art_optimization_to_dhis()
