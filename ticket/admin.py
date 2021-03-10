from django.contrib import admin
from .models import Ticket,Ticket_info,Order,Payment,Printticket,Cancelticket
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Ticket_info)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Printticket)
admin.site.register(Cancelticket)
