from django.db import models

# class ArvDispensing(models.Model):
#     province = models.CharField(max_length = 150)
#     district = models.CharField(max_length = 150, blank=True, null=True)
#     health_facility = models.CharField(max_length = 150)
#     patient_id = models.IntegerField()
#     patient_name = models.CharField(max_length = 255)
#     patient_identifier = models.CharField(max_length =255)
#     age = models.IntegerField()
#     phone_number = models.CharField(max_length = 150, null=True, blank=True)
#     dispensing_date = models.DateField()
#     next_dispensing_date =  models.DateField()
#     gender = models.CharField(max_length = 150)
#     community = models.CharField(max_length = 500, blank=True, null=True)
#     pregnant = models.CharField(max_length =10, default="NAO")
#     brestfeeding = models.CharField(max_length =10, default="NAO")
#     tb = models.CharField(max_length =10, default="NAO")
    
#     def __str__(self):
#         return self.patient_name
    
class Visit(models.Model):
    type_visit = models.CharField(max_length=150)
    province = models.CharField(max_length = 150)
    district = models.CharField(max_length = 150, blank=True, null=True)
    health_facility = models.CharField(max_length = 150)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length = 255)
    patient_identifier = models.CharField(max_length =255)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 150, null=True, blank=True)
    appointment_date = models.DateField()
    next_appointment_date =  models.DateField()
    gender = models.CharField(max_length = 150)
    community = models.CharField(max_length = 500, blank=True, null=True)
    pregnant = models.CharField(max_length =10, default="NAO")
    brestfeeding = models.CharField(max_length =10, default="NAO")
    tb = models.CharField(max_length =10, default="NAO")
    
    def __str__(self):
        return self.patient_name
