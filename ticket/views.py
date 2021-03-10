from django.shortcuts import render,get_object_or_404
from .models import Ticket,Ticket_info,Order,Payment,Cancelticket
from .form import TicketForm,Paymentform,Print_ticket,Cancel_ticket
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def show_info(request):
    ticket_list = Ticket_info.objects.all()

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            source_id = form.cleaned_data['source_id']
            destination_id = form.cleaned_data['destination_id']
            start_time = form.cleaned_data['start_time']
            date = form.cleaned_data['date']



            ticket_list = Ticket_info.objects.filter(source_id__station_name__contains=source_id,
                                                     destination_id__station_name__contains=destination_id,
                                                     start_time__time_slot__contains=start_time,
                                                     date__contains=date
                                                     )



    context = {
        'tickets': ticket_list
    }

    return render(request, 'ticket/show.html', context)


@login_required
def BookTicket(request):

    form = TicketForm()


    if request.method  == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            source_id = form.cleaned_data['source_id']
            destination_id = form.cleaned_data['destination_id']
            start_time = form.cleaned_data['start_time']
            date = form.cleaned_data['date']




            ticket_list = Ticket_info.objects.filter(source_id__station_name__contains=source_id,
                                                     destination_id__station_name__contains=destination_id,
                                                     start_time__time_slot__contains = start_time,
                                                     date__contains=date
                                                     )


            context = {
                'tickets': ticket_list
            }
            return render(request, 'ticket/show.html', context)


    context= {
        'Ticketforms':form
    }
    return render(request,'ticket/BookTicket.html',context)

@login_required
def make_order(request,ticket_id):
    tic=Ticket_info.objects.all()
    ticket = get_object_or_404(Ticket_info, id=ticket_id)
    order = Order(user=request.user, ticket=ticket)
    ticket.avaible_seat-=1





    order.save()
    context={
                'order':order,
                'ticket':ticket
            }

    return render(request,'ticket/show_ticket.html',context)

@login_required
def make_payment(request,ticket_id):
    messages=''
    form=Paymentform()
    ticket = get_object_or_404(Ticket_info, id=ticket_id)
    #order = Payment(user=request.user, ticket=ticket)
    if request.method =="POST":
        form=Paymentform(request.POST)
        if form.is_valid():
            transaction_id=form.cleaned_data['transaction_id']
            #payment_options =form.cleaned_data[' payment_options']
            payment=Payment(user=request.user, ticket=ticket,transaction_id=transaction_id)
            payment.save()
            messages="Your Payment Is successful"

    context={
        'form':form,
        'ticket':ticket,
        'messages':messages
    }
    return render(request, 'ticket/payment.html', context)
@login_required
def print_ticket(request):
    form = Print_ticket()
    Or= Order.objects.all()

    if request.method == "POST":
        form = Print_ticket(request.POST)
        if form.is_valid():
            user=request.user
            ticket=form.cleaned_data['ticket']

            ticket_list = Ticket_info.objects.filter( id__contains=ticket)
            order=Order.objects.filter(user__username__contains=user,
                                       ticket__id__contains=ticket)
            for o in Or:
                if o.user==user:
                    if o.ticket==ticket:
                        if o.status=="Approved":
                            context={

                                    'user':user,
                                    'ticket_list':ticket_list
                                                    }
                            return render(request,'ticket/ticketinfo.html',context)
                        else:
                            messages="Your Payment is under process.You will get your ticket soon"
                            context = {

                                'messages': messages
                            }
                            return render(request, 'ticket/ticketinfo.html', context)
                    else:
                        messages = "Your Ticket is not found.Please book a ticket."
                        context = {

                            'messages': messages
                        }
                        return render(request, 'ticket/ticketinfo.html', context)

    context = {
        'Ticketforms': form
    }
    return render(request, 'ticket/searchownticket.html', context)
@login_required
def orderhistory(request):
    user = request.user
    try:

        Or = Order.objects.filter(user=request.user)
        user=request.user
        for o in Or:
            if o.user == user:
                context = {

                         'o': Or
                        }
                return render(request, 'ticket/history.html', context)
    except Order.DoesNotExist:
        Or = "You don't have any order"
    context = {

            'o': Or
        }
    return render(request, 'ticket/history.html', context)



@login_required
def cancelticket(request):
    message=''
    form=Cancel_ticket()
    if request.method == "POST":
        form = Cancel_ticket(request.POST)

        if form.is_valid():
            cancel = form.save(commit=False)
            cancel.user=request.user
            cancel.save()
            message='Your Request Is In Queue'

    context = {
        'cancel': form,
        'messages':message
    }

    return render(request, 'ticket/cancelticket.html', context)

@login_required
def cancelhistory(request):
    try:

        Or = Cancelticket.objects.filter(user=request.user)
        user=request.user
        for o in Or:
            if o.user == user:

                context = {

                    'o': Or
                }
                return render(request, 'ticket/Cancelhistory.html', context)

    except Cancelticket.DoesNotExist:
        Or='You donot have any cancelation'

    context = {

        'o': Or
    }
    return render(request, 'ticket/Cancelhistory.html', context)











