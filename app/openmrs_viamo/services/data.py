import requests
from  django.db.models import Q
from openmrs_viamo.models import Visit
from datetime import datetime, timedelta, date

API_URL_ARV = 'http://197.218.241.174:8080/csn4/ws/rest/v1/reportingrest/dataSet/ffeed60a-2a94-4875-80cd-4baca75f13d4'
API_URL_AP = 'http://197.218.241.174:8080/csn4/ws/rest/v1/reportingrest/dataSet/9bceb29a-f9eb-4695-96ba-e5ae664aa0df'

start_date = date.today()  + timedelta(days=4)
end_date = start_date + timedelta(days=4)
params = {
    'startDate': str(start_date),
    'endDate': str(end_date)
}

def retrieve_art_dispensing():
    try: 
        response = requests.get(API_URL_ARV, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
        data_list = response.json()['rows']
        for data in data_list:
            # province, created = Province.objects.get_or_create(name='Tete')
            # district, created = District.objects.get_or_create(name=data['Distrito'], province=province)
            # health_facility, created = HealthFacility.objects.get_or_create(name=data['us'], district=district)
            visit, created = Visit.objects.get_or_create(
                type_visit='ART Dispensing',
                province='Tete',
                district=data['Distrito'],
                health_facility=data['us'],
                patient_id=data['patient_id'],
                patient_name=data['NomeCompleto'],
                patient_identifier=data['NID'], 
                age=data['age'],
                phone_number=data['phone_number'],
                appointment_date=datetime.fromtimestamp(data['dispensing_date'] / 1e3),
                next_appointment_date=datetime.fromtimestamp(data['next_dispensing_date'] / 1e3),
                gender=data['gender'],
                community=data['Bairro'],
                pregnant=data['pregnant'],
                brestfeeding=data['brestfeeding'],
                tb=data['tb']

            )

            # province.save()
            # district.save()
            # health_facility.save()
            visit.save()  
            
    except requests.exceptions.RequestException as err:
        print(err, API_URL)
        
        
def retrieve_appointments():
    try: 
        response = requests.get(API_URL_AP, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
        # print(response.text)
        data_list = response.json()['rows']
        for data in data_list:
            # province, created = Province.objects.get_or_create(name='Tete')
            # district, created = District.objects.get_or_create(name=data['Distrito'], province=province)
            # health_facility, created = HealthFacility.objects.get_or_create(name=data['us'], district=district)
            visit, created = Visit.objects.get_or_create(
                type_visit='Appointment',
                province='Tete',
                district=data['Distrito'],
                health_facility=data['us'],
                patient_id=data['patient_id'],
                patient_name=data['NomeCompleto'],
                patient_identifier=data['NID'], 
                age=data['age'],
                phone_number=data['phone_number'],
                appointment_date=datetime.fromtimestamp(data['appointment_date'] / 1e3),
                next_appointment_date=datetime.fromtimestamp(data['next_appointment_date'] / 1e3),
                gender=data['gender'],
                community=data['Bairro'],
                pregnant=data['pregnant'],
                brestfeeding=data['brestfeeding'],
                tb=data['tb']

            )

            # province.save()
            # district.save()
            # health_facility.save()
            visit.save()  
            
    except requests.exceptions.RequestException as err:
        print(err, API_URL_AP)     
                
                
def post_data_to_server():
    URL = ' https://go.votomobile.org/api/v1/subscribers'
    API_KEY = '5e210b5942d9362ae1e50f49f'
    startDate = date.fromisoformat('2021-06-10')
    endDate = date.fromisoformat('2021-06-16')
    payload_list = []
    visit = Visit.objects.exclude(phone_number=None).filter(next_appointment_date__range=(start_date, end_date), health_facility__in = ['CS Nº 3 - Bairro Manyanga', 'CS Nº 4 - Bairro Muthemba'])
    for v in visit: 
        phone = v.phone_number.strip()
        payload = {
            "api_key": API_KEY,
            "phone": phone[:9],
            "receive_voice": "1",
            "receive_sms": "1",
            "preferred_channel": "1",
            "groups": "463089",
            "active": "1",
        }
    
        data_values = {
             "patient_identifier": v.patient_identifier,
             "appointment_date": '{:%Y-%m-%d}'.format(v.next_appointment_date),
             "actual_visit_date": '{:%Y-%m-%d}'.format(v.appointment_date),
             "gender": v.gender,
             "pregnant": v.pregnant,
             "age": v.age,
             "district": v.district,
             "province": v.province,
             "health_facility": v.health_facility
        }
        
        payload['property'] = data_values
        payload_list.append(payload)
        
    print(payload_list)
    print(f'{len(payload_list)} records will be sent....')
    records = 0
    try:
        for data in payload_list:
            records += 1
            response = requests.post(URL, json=data)
            print(f'Sending {records} of {len(payload_list)} Records')
            print(response.raise_for_status)
         
    except requests.exceptions.RequestException as err:
        print(err, URL)
    
    