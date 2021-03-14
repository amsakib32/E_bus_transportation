from django.shortcuts import render
from .models import Payment
# Create your views here.
def show_info(request):
    pay_list=Payment.objects.all()
    context={
        'pays':pay_list
    }
    return render(request,'payment/show.html',context)
