from django.db import models

# Create your models here.
class Time(models.Model):
    time_slot=models.TimeField(unique=True)

    def __str__(self):
        return str(self.time_slot)
