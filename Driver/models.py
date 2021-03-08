from django.db import models

# Create your models here.
class Driver(models.Model):
    name=models.CharField(max_length=200)
    contact=models.IntegerField()
    n_id=models.CharField(max_length=30)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.name
