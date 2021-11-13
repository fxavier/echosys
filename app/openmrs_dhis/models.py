from django.db import models
from core.models import Province

class OpenmrsOptimization(models.Model):
    elegiveisdtg = models.IntegerField()
    dtg_geral = models.IntegerField()
    elegiveislpvr_geral = models.IntegerField()
    dtg = models.IntegerField()
    em_tarv = models.IntegerField()
    lpvr = models.IntegerField()
    elegiveis_lpvr = models.IntegerField()
    elegiveisdtg_geral = models.IntegerField()
    lpvr_geral = models.IntegerField()
    us = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.us} {self.period}'
    
