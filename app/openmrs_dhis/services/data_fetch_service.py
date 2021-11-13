import requests
import time
from datetime import datetime, timedelta

from core.models import HealthFacility, Province, District, OpenmrsURL, DataElement, DataElementValue
from openmrs_dhis.models import OpenmrsOptimization


 
def fetch_openmrs_optimization_data(): 
    openmrs_url = OpenmrsURL.objects.exclude(province='Sofala')
    startDate = datetime.now() - timedelta(days=32)
    endDate = startDate + timedelta(days=29)
    period = endDate.strftime('%Y%m')
    params = {
        'startDate': str(startDate.strftime('%Y-%m-%d')),
        'endDate': str(endDate.strftime('%Y-%m-%d'))
    }
    for openmrs in openmrs_url:
        try:
            base_url = openmrs.url 
            uuid = openmrs.uuid
            API_URL = f'{base_url}{uuid}'
            params['location'] = openmrs.instance_name
            response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
            print(f'{base_url} {params}')
            print(response.text)
            # json_data = response.json()['rows']
        
            # for data in json_data:
            #     us = ""
            #     data_dict = {}
            #     for key, value in data.items(): 
            #         if key == 'id':
            #             continue
            #         elif key == 'us':
            #             us = value
            #             continue
            #         else:
            #             data_dict[key] = value
                        
            #     for key, value in data_dict.items():
            #         dataElement = DataElement.objects.get(openmrs=key)
            #         healthFacility = HealthFacility.objects.get(name=openmrs.instance_name)
            #         dataElementValue, created = DataElementValue.objects.get_or_create(
            #             period=period,
            #             value=value,
            #             healthFacility=healthFacility,
            #             dataElement=dataElement
            #         )
            #         dataElementValue.save()
            # print(openmrs.instance_name)
            time.sleep(60 * 3)
        except requests.exceptions.RequestException as err: 
            print(err, API_URL)
               
                        
                           
# def get_optimization_data():
#     startDate = datetime.now() - timedelta(days=28)
#     endDate = startDate + timedelta(days=29)
#     period = endDate.strftime('%Y%m')
#     params = {
#         'startDate': str(startDate.strftime('%Y-%m-%d')),
#         'endDate': str(endDate.strftime('%Y-%m-%d')),
#         'location': 'CS Magoe'
#     }
    
#     try:
#         API_URL = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/ef736830-ccca-4a17-a93f-d8fbb8e3baa7'
        
    #     response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
    #     json_data = response.json()['rows']
    #     print(json_data)
    #     for data in json_data:
    #        healthFacility, created = HealthFacility.objects.get_or_create(name=data['us'])
    #        province, created = Province.objects.get_or_create(name='Tete')
    #        openmrs_optimization, created = OpenmrsOptimization.objects.get_or_create(
    #             elegiveisdtg=data['elegiveisdtg'],
    #             dtg_geral=data['dtg_geral'],
    #             elegiveislpvr_geral=data['elegiveislpvr_geral'],
    #             dtg=data['dtg'],
    #             em_tarv=data['em_tarv'],
    #             lpvr=data['lpvr'],
    #             elegiveis_lpvr=data['elegiveis_lpvr'],
    #             elegiveisdtg_geral=data['elegiveisdtg_geral'], 
    #             lpvr_geral=data['lpvr_geral'],
    #             us=healthFacility,
    #             periodo=period,
    #             province=province
    #                     )
    #        openmrs_optimization.save()
    #        print(data)
                
    # except requests.exceptions.RequestException as err: 
    #     print(err, API_URL)


# def get_openmrs_optimization(self): 
#         startDate = datetime.now() - timedelta(days=37)
#         endDate = startDate + timedelta(days=30)
#         period = endDate.strftime('%Y%m')
#         params = {
#             'startDate': str(startDate.strftime('%Y-%m-%d')),
#             'endDate': str(endDate.strftime('%Y-%m-%d'))
#         }
        
#         try:
#             API_URL = 'http://197.218.206.34:8080/openmrs/ws/rest/v1/reportingrest/dataSet/3443cd92-c2ea-4932-afa0-b58986476fbb'
            
#             response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
#             json_data = response.json()['rows']
#             for data in json_data:
#                 us = ""
#                 data_dict = {}
#                 for key, value in data.items(): 
#                     if key == 'id':
#                         continue
#                     elif key == 'us':
#                         us = value
#                         continue
#                     else:
#                         data_dict[key] = value
                        
#                 for key, value in data_dict.items():
#                     dataElement = DataElement.objects.get(openmrs=key)
#                     healthFacility = HealthFacility.objects.get(name=us)
#                     dataElementValue, created = DataElementValue.objects.get_or_create(
#                         period=period,
#                         value=value,
#                         healthFacility=healthFacility,
#                         dataElement=dataElement
#                     )
#                     dataElementValue.save()
                    
#         except requests.exceptions.RequestException as err: 
#             print(err, API_URL)

