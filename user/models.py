
from django.db import models
from django.contrib.auth.models import User
from ticket.models import Ticket_info
# Create your models here.
class Profile(models.Model):
    Date_Of_Birth=models.DateField(null=True)
    contact=models.IntegerField()
    n_id=models.CharField(max_length=30)
    address=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Customercare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Complain=models.TextField(max_length=1000)
    CHOICES = (
        ('Complain against Driver', 'Complain against Driver'),
        ('Complain against BUS Service', 'Complain against Bus Service'),
        ('Complain against Booking System', 'Complain against Booking System'),
        ('Facing other Problem', 'Facing other Problem')
    )
    Options = models.CharField(max_length=50, choices=CHOICES, default='Facing other Problem')

    def __str__(self):
        return self.user.username

class Smsticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_no=models.IntegerField()
    Ticket_no=models.ForeignKey(Ticket_info, on_delete=models.CASCADE, null=True, blank=True)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username





