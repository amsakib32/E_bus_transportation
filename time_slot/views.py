from django.shortcuts import render
from django.shortcuts import render

from .models import Time
# Create your views here.
def show_info(request):
    time_list=Time.objects.all()
    context={
        'times':time_list
    }
    return render(request,'time/show.html',context)

