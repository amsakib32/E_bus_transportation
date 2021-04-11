"""e_bus_transportation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as users
from time_slot import views as time
from station import views as station
from bus import views as bus
from Driver import views as driver
from payment import views as payment
from ticket import views as ticket

urlpatterns = [
path('admin/', admin.site.urls),
    path('showprofile/', users.show_info,name='showprofile'),
    path('time/', time.show_info,name='time'),
    path('station/', station.show_info,name='station'),
    path('bus/', bus.show_info,name='bus'),
    path('use/', bus.use_show_info,name='use'),
    path('payment/',payment.show_info,name='payment'),
    path('ticket/',ticket.show_info,name='ticket'),
    path('registration/',users.UserReg,name='registration'),
    path('profilecreate/',users.ProfileCreate,name='profilecreate'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',ticket.BookTicket,name='bookticket'),
    path('orderticket/<int:ticket_id>',ticket.make_order,name='orderticket'),
    path('payment/<int:ticket_id>',ticket.make_payment,name='payment'),
    path('customercare/',users.customercare,name='customercare'),
    path('smsticket/', users.smsticket, name='smsticket'),
    path('printticket', ticket.print_ticket, name='printticket'),
    path('bookedhistory', ticket.orderhistory, name='history'),
    path('cancelticket', ticket.cancelticket, name='cancel'),
    path('cancelhistory', ticket.cancelhistory, name='cancelhistory'),

]
