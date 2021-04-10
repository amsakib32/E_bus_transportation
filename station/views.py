from django.shortcuts import render
from .models import Station
# Create   your views here .
def show_info(request):
    station_list=Station.objects.all()
    context={
        'stations':station_list
    }
    return render(request,'station/show.html',context)
