from django import forms
from .models import Ticket,Payment,Printticket,Cancelticket


class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields = ['source_id', 'destination_id','start_time','date']

class Paymentform(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['transaction_id','payment_options']

class Print_ticket(forms.ModelForm):
    class Meta:
        model=Printticket
        fields=['ticket']

class Cancel_ticket(forms.ModelForm):
    class Meta:
        model=Cancelticket
        fields=['ticket']