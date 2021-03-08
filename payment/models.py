from django.db import models
from user.models import Profile
from ticket.models import Ticket
# Create your models here.
class Payment(models.Model):
    total_bill=models.FloatField(null=True)
    payment_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    ticket_id=models.ForeignKey(Ticket,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user_id