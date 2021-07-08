from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs_viamo.services.data import retrieve_art_dispensing, retrieve_appointments, \
                                       post_data_to_server


@shared_task
def get_appointment_data(): 
    retrieve_appointments()

@shared_task
def get_art_data():
    retrieve_art_dispensing()
    
@shared_task    
def post_data(): 
    post_data_to_server()
