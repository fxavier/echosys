import requests
from datetime import datetime, timedelta, date
from openmrs.models import Paciente, Location, ConsultaClinica, Inscricao, Fila
from core.utils.data_conversion import DataConversion

# location_url = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/5cd2ea5b-b11f-454b-9b45-7a78ac33eab9'
# inscritos_url = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/e386ec30-689b-4e43-b6fc-587bac266ea4'
# inscritos_niassa = http://197.218.206.34:8080/openmrs/ws/rest/v1/reportingrest/dataSet/b36d7f18-2af9-4025-983a-5e6fc2e29c8a
# location_niassa = http://197.218.206.34:8080/openmrs/ws/rest/v1/reportingrest/dataSet/331da8bc-e426-4679-b55a-29dbafe79f8a


class PullOpenmrsData:
    URL_BASE = 'http://197.218.206.34:8080/openmrs/ws/rest/v1/reportingrest/dataSet/'

    def get_locations(self, uuid):
        url = PullOpenmrsData.URL_BASE + uuid
        try:
            response = requests.get(url, auth=('xavier.nhagumbe', 'Goabtgo1'))
            locations_list = response.json()['rows']
            return locations_list
        except requests.exceptions.RequestException as err:
            print(err)

    def get_patients(self, uuid, params: dict):
        url = PullOpenmrsData.URL_BASE + uuid
        try:
            response = requests.get(url, params=params, auth=(
                'xavier.nhagumbe', 'Goabtgo1'))
            patient_list = response.json()['rows']
            return patient_list
        except requests.exceptions.RequestException as err:
            print(err)

    def get_consulta_clinica(self, uuid, params: dict):
        url = PullOpenmrsData.URL_BASE + uuid
        try:
            response = requests.get(url, params=params, auth=(
                'xavier.nhagumbe', 'Goabtgo1'))
            consulta = response.json()['rows']
            return consulta
        except requests.exceptions.RequestException as err:
            print(err)

    def get_levantamento(self, uuid, params: dict):
        url = PullOpenmrsData.URL_BASE + uuid
        try:
            response = requests.get(url, params=params, auth=(
                'xavier.nhagumbe', 'Goabtgo1'))
            fila = response.json()['rows']
            return fila
        except requests.exceptions.RequestException as err:
            print(err)


class AddDataToMiddleware:

    def add_locations(self):
        data_list = PullOpenmrsData().get_locations(
            '331da8bc-e426-4679-b55a-29dbafe79f8a')
        print(data_list)

        if data_list is not None:
            for data in data_list:
                location, created = Location.objects.get_or_create(
                    location_id=data['location_id'],
                    codigo=data['ID'],
                    name=data['NAME'],
                    description=data['description'],
                    state_province=data['state_province'],
                    country=data['country'],
                    parent_location=data['parent_location']


                )
                location.save()
        else:
            print('No records!')

    def add_patient(self):
        params = {
            'startDate': '2021-11-01',
            'endDate': '2021-11-10'
        }
        patients = PullOpenmrsData().get_patients(
            'b36d7f18-2af9-4025-983a-5e6fc2e29c8a', params)
        print(patients)
        if patients is not None:
            for data in patients:
                location = Location.objects.get(location_id=data['location'])
                paciente, created = Paciente.objects.get_or_create(
                    patient_id=data['patient_uuid'],
                    nid=data['NID'],
                    nome=data['NomeCompleto'],
                    genero=data['gender'],
                    data_nascimento=DataConversion.convert_openmrs_date(
                        data['data_nascimento']),
                    telefone=data['telefone'],
                    distrito=data['Distrito'],
                    posto_administrativo=data['PAdministrativo'],
                    localidade=data['Localidade'],
                    bairro=data['Bairro'],
                    ponto_referencia=data['PontoReferencia']
                )

                paciente.save()

                inscricao, created = Inscricao.objects.get_or_create(
                    paciente=paciente,
                    data_abertura=DataConversion.convert_openmrs_date(
                        data['data_abertura']),
                    data_diagnostico=DataConversion.convert_openmrs_date(
                        data['data_diagnostico']),
                    inscrito_programa=data['inscrito_programa'],
                    data_inscricao_programa=DataConversion.convert_openmrs_date(
                        data['data_inscricao_programa']),
                    data_inicio_tarv=DataConversion.convert_openmrs_date(
                        data['data_inicio']),
                    morreu=data['dead'],
                    data_morte=DataConversion.convert_openmrs_date(
                        data['death_date']),
                    referencia=data['referencia'],
                    estadio_oms=data['valor_estadio'],
                    data_estadio_oms=DataConversion.convert_openmrs_date(
                        data['data_estadio']),
                    transferido_em=data['transferido_de'],
                    data_transferencia=DataConversion.convert_openmrs_date(
                        data['data_transferido_de']),
                    location=location
                )

                inscricao.save()
        else:
            print('No records!')

    def add_consulta_clinica(self, params):
        consulta = PullOpenmrsData().get_consulta_clinica(
            'fb6f6702-ae98-468c-824e-1d9b32001f02', params)
        print(consulta)
        if consulta is not None:
            for data in consulta:
                # paciente = Paciente.objects.get(
                #     patient_id=data['patient_uuid'])
                location = Location.objects.get(location_id=data['location'])

                paciente, created = Paciente.objects.get_or_create(
                    patient_id=data['patient_uuid'],
                    nid=data['NID'],
                    nome=data['NomeCompleto'],
                    genero=data['gender'],
                    data_nascimento=DataConversion.convert_openmrs_date(
                        data['data_nascimento']),
                    telefone=data['telefone'],
                    distrito=data['Distrito'],
                    posto_administrativo=data['PAdministrativo'],
                    localidade=data['Localidade'],
                    bairro=data['Bairro'],
                    ponto_referencia=data['PontoReferencia']
                )
                paciente.save()

                consulta, created = ConsultaClinica.objects.get_or_create(
                    data_consulta=DataConversion.convert_openmrs_date(
                        data['data_consulta']),
                    paciente=paciente,
                    data_proxima_consulta=DataConversion.convert_openmrs_date(
                        data['proxima_consulta']),
                    gravidez=data['gravida'],
                    lactante=data['lactante'],
                    tratamento_tb=data['tb'],
                    location=location
                )
                consulta.save()

        else:
            print('No records!')

    def add_levantamento(self, params):
        fila = PullOpenmrsData().get_levantamento(
            '534d8598-a52a-4365-b4dd-5fb61b57300f', params)
        print(fila)

        if fila is not None:
            for data in fila:
                location = Location.objects.get(location_id=data['location'])
                paciente, created = Paciente.objects.get_or_create(
                    patient_id=data['patient_uuid'],
                    nid=data['NID'],
                    nome=data['NomeCompleto'],
                    genero=data['gender'],
                    data_nascimento=DataConversion.convert_openmrs_date(
                        data['data_nascimento']),
                    telefone=data['telefone'],
                    distrito=data['Distrito'],
                    posto_administrativo=data['PAdministrativo'],
                    localidade=data['Localidade'],
                    bairro=data['Bairro'],
                    ponto_referencia=data['PontoReferencia']
                )
                paciente.save()

                fila, created = Fila.objects.get_or_create(
                    data_inicio_tarv=DataConversion.convert_openmrs_date(
                        data['data_inicio']),
                    data_levantamento=DataConversion.convert_openmrs_date(
                        data['ultimo_levantamento']),
                    regime=data['ultimo_regime'],
                    quantidade=data['quantidade'],
                    data_proximo_levantamento=DataConversion.convert_openmrs_date(
                        data['proximo_marcado']),
                    paciente=paciente,
                    location=location
                )
                fila.save()
        else:
            print('No records!')
