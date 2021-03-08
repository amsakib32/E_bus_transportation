from django.shortcuts import render
from .models import Bus,Use
# Create your views here.
def show_info(request):
    bus_list=Bus.objects.all()
    context={
        'buses':bus_list
    }
    return render(request,'bus/show.html',context)
def use_show_info(request):
    use_list=Use.objects.all()
    context={
        'uses':use_list
    }
    return render(request,'bus/use.html',context)