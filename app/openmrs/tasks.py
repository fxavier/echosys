from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs.services.data_service import AddDataToMiddleware

params = {
    'startDate': '2021-11-01',
    'endDate': '2021-11-10'
}


@shared_task
def add_locations():
    AddDataToMiddleware().add_locations()


@shared_task
def add_patient():
    AddDataToMiddleware().add_patient()


@shared_task
def add_consulta():
    AddDataToMiddleware().add_consulta_clinica(params)


@shared_task
def add_levantamento():
    AddDataToMiddleware().add_levantamento(params)
