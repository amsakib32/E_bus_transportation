from django.db import models
from station.models import Station
from Driver.models import Driver
# Create your models here.
class Bus(models.Model):
    bus_name=models.CharField(max_length=200)
    bus_type=models.CharField(max_length=10)
    driver_id=models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.bus_name

class Use(models.Model):
    bus_id=models.ForeignKey(Bus,on_delete=models.CASCADE)
    station_id=models.ForeignKey(Station,on_delete=models.CASCADE)



    def __str__(self):
        return self.bus_id