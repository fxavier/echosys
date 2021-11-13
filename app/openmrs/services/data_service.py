import requests
from datetime import datetime, timedelta, date
from openmrs.models import Paciente, Location, ConsultaClinica

# location_url = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/5cd2ea5b-b11f-454b-9b45-7a78ac33eab9'
# inscritos_url = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/e386ec30-689b-4e43-b6fc-587bac266ea4'


class PullOpenmrsData:
    URL_BASE = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/'

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


class AddDataToMiddleware:

    def add_locations(self):
        data_list = PullOpenmrsData().get_locations(
            '5cd2ea5b-b11f-454b-9b45-7a78ac33eab9')
        print(data_list)

        if data_list is not None:
            for data in data_list:
                location, created = Location.objects.get_or_create(
                    location_id=data['location_id'],
                    codigo=data['codigo'],
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
            'startDate': '1900-01-01',
            'endDate': '2021-11-10'
        }
        patients = PullOpenmrsData().get_patients(
            'e386ec30-689b-4e43-b6fc-587bac266ea4', params)
        print(patients)
        if patients is not None:
            for data in patients:
                paciente, created = Paciente.objects.get_or_create(
                    patient_id=data['patient_uuid'],
                    nid=data['NID'],
                    nome=data['NomeCompleto'],
                    genero=data['gender'],
                    data_nascimento=datetime.fromtimestamp(
                        data['data_nascimento'] / 1e3),
                    telefone=data['telefone'],
                    distrito=data['Distrito'],
                    posto_administrativo=data['PAdministrativo'],
                    localidade=data['Localidade'],
                    bairro=data['Bairro'],
                    ponto_referencia=data['PontoReferencia']
                )

            paciente.save()
        else:
            print('No records!')

    # patient_id = models.CharField(max_length=500, primary_key=True)
    # nid = models.CharField(max_length=255)
    # nome = models.CharField(max_length=255)
    # genero = models.CharField(max_length=20)
    # data_nascimento = models.DateTimeField()
    # telefone = models.CharField(max_length=100, blank=True, null=True)
    # profissao = models.CharField(max_length=100, blank=True, null=True)
    # livro = models.CharField(max_length=15, blank=True, null=True)
    # pagina = models.CharField(max_length=4, blank=True, null=True)
    # linha = models.CharField(max_length=4, blank=True, null=True)
    # nome_confidente = models.CharField(max_length=255, blank=True, null=True)
    # confidente_parentesco = models.CharField(
    #     max_length=255, blank=True, null=True)
    # telefone1_confidente = models.CharField(
    #     max_length=255, blank=True, null=True)
    # telefone2_confidente = models.CharField(
    #     max_length=255, blank=True, null=True)
    # endereco_confidente = models.CharField(
    #     max_length=500, null=True, blank=True)
    # distrito = models.CharField(max_length=100, null=True, blank=True)
    # posto_administrativo = models.CharField(
    #     max_length=100, null=True, blank=True)
    # localidade = models.CharField(max_length=100, null=True, blank=True)
    # bairro = models.CharField(max_length=100, null=True, blank=True)
    # ponto_referencia = models.CharField(max_length=100, null=True, blank=True)

    #   "valor_estadio": "I",
    #   "location": "5a04df3e-692f-4cc8-8abe-3807ffd0c5bd",
    #   "transferido_de": null,
    #   "data_inscricao_programa": null,
    #   "gender": "F",
    #   "PontoReferencia": null,
    #   "data_aceita": null,
    #   "dead": false,
    #   "NomeCompleto": "Joana Alberto Alberto",
    #   "Distrito": "Chiuta",
    #   "inscrito_programa": "NAO",
    #   "death_date": null,
    #   "PAdministrativo": "Manje",
    #   "data_abertura": 1612821600000,
    #   "data_inicio": 1325628000000,
    #   "data_nascimento": "1999-01-01",
    #   "data_estadio": 1630274400000,
    #   "referencia": null,
    #   "data_transferido_de": null,
    #   "data_seguimento": 1630274400000,
    #   "telefone": null,
    #   "Localidade": "Manje-sede",
    #   "patient_uuid": "bf3f9bf1-b274-412f-aab6-f691b5a22ce3",
    #   "patient_id": 9371,
    #   "Bairro": null,
    #   "data_diagnostico": null,
    #   "NID": "0105060801/2008/00012"
