from django.db import models

# Create Station.
class Station(models.Model):
    station_name=models.CharField(max_length=200)

    def __str__(self):
        return self.station_name