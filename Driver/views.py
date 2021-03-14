from django.shortcuts import render
from .models import Driver
# Create your views here.
def show_info(request):
    driver_list=Driver.objects.all()
    context={
        'drivers':driver_list
    }
    return render(request,'driver/driver.html',context)

