from django.db import models
from django.db.models.fields import DateField
from django.db.models.signals import pre_save, post_save
from core.utils.constants import Constants


MES = (
    ('Jan', 'Janeiro'),
    ('Feb', 'Fevereiro'),
    ('Mar', 'Março'),
    ('Apr', 'Abril'),
    ('May', 'Maio'),
    ('Jun', 'Junho'),
    ('Jul', 'Julho'),
    ('Aug', 'Agosto'),
    ('Sep', 'Setembro'),
    ('Oct', 'Outubro'),
    ('Nov', 'Novembro'),
    ('Dec', 'Dezembro')
)

class Province(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class District(models.Model):
    """Model definition for District."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    province = models.ForeignKey('Province', on_delete=models.CASCADE)
   
    def __str__(self):
        """Unicode representation of District."""
        return self.name

class HealthFacility(models.Model):
    """Model definition for HealthFacility."""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    # openmrs_name = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for HealthFacility."""

        verbose_name = 'Health Facility'
        verbose_name_plural = 'Health Facilities'

    def __str__(self):
        """Unicode representation of HealthFacility."""
        return self.name

    
class DataSet(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.name


class DataElement(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    openmrs = models.CharField(max_length=100, null=True, blank=True)
    categoryOptionCombo = models.CharField(max_length=200, null=True, blank=True)
    attributeOptionCombo = models.CharField(max_length=200, null=True, blank=True)
    dataSet = models.ForeignKey(DataSet, on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.name

class DataElementValue(models.Model):
    period = models.CharField(max_length=100)
    value = models.IntegerField(null=True, blank=True) 
    healthFacility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    dataElement = models.ForeignKey('DataElement', on_delete=models.CASCADE)
    synced = models.BooleanField(default=False)
    
    def __str__(self):
        return self.dataElement.name
    
class OpenmrsURL(models.Model): 
    province = models.CharField(max_length=100)
    openmrs_us = models.CharField(max_length=100, null=True, blank=True)
    instance_name = models.CharField(max_length=100)
    uuid = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    dataSet = models.ForeignKey(DataSet, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.province} {self.instance_name}'
    
class PeriodDescription(models.Model):
    ano = models.CharField(max_length=10)
    mes = models.CharField(max_length = 50, choices=MES)
    period_ref = models.CharField(max_length=100, null=True, blank=True)
    period = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.period_ref)
    
def create_ref_and_period(sender, instance, created, *args, **kwargs): 
    if created:
        constants = Constants()
        key_list = list(constants.get_months().keys())
        val_list = list(constants.get_months().values())
        obj = PeriodDescription.objects.get(id=instance.id)
        obj.period_ref = f'{obj.mes} {obj.ano}'
        mes_ref = obj.mes
        obj.period = f'{obj.ano}{key_list[val_list.index(mes_ref)]}'
        obj.save()
        
post_save.connect(create_ref_and_period, sender=PeriodDescription)   
