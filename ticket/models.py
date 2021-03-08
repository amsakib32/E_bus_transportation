from django.db import models
from django.contrib.auth.models import User
from time_slot.models import Time
from station.models import Station
from bus.models import Bus

# Create your models here.
class Ticket(models.Model):
    start_time=models.ForeignKey(Time,on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    source_id = models.ForeignKey(Station, on_delete=models.CASCADE,related_name='+',null=True)
    destination_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+',null=True)
    number_of_tickets = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return str(self.start_time)


class Ticket_info(models.Model):
    start_time = models.ForeignKey(Time, on_delete=models.CASCADE,null=True)
    source_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    destination_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    price=models.FloatField(null=False)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    avaible_seat=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return str(self.id)

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket_info, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved')
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.username)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    ticket = models.ForeignKey(Ticket_info, on_delete=models.CASCADE, null=True, blank=True)
    transaction_id=models.CharField(max_length=200,null=True,blank=True)
    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket')
    )
    payment_options = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Bkash')

    def __str__(self):
        return str(self.user.username)

class Printticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.ForeignKey(Ticket_info, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Cancelticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.ForeignKey(Ticket_info, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected','Rejected'),
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.user.username)

