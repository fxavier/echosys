from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs.services.data_service import AddDataToMiddleware


@shared_task
def add_locations():
    AddDataToMiddleware().add_locations()


@shared_task
def add_patient():
    AddDataToMiddleware().add_patient()
