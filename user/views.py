from django.shortcuts import render
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import ProfileForm,Customerform,Smsticketform
from django.contrib.auth.decorators import login_required
from .form import UserCreationForm
# Create your views here.
@login_required
def show_info(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile to view"
    context = {
        'user': profile
    }
    return render(request, 'user/show.html', context)

def UserReg(request):
    userform = UserCreationForm()


    if request.method  == "POST":
        userform = UserCreationForm(request.POST)

        if userform.is_valid():
            userform.save()
            messages.success(request,'successfully created user account')
        else:
            messages.MessageFailure(request,'Sorry your account is not created try again')

    context= {
        'userforms':userform
    }
    return render(request,'user/reg.html',context)

@login_required
def ProfileCreate(request):
    form = ProfileForm()


    if request.method  == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'successfully created user account')

    context= {
        'Profileforms':form
    }
    return render(request,'user/createprofile.html',context)
@login_required
def customercare(request):
    messages=''
    form=Customerform()
    if request.method == "POST":
        form = Customerform(request.POST)

        if form.is_valid():
            complane = form.save(commit=False)
            complane.user = request.user
            complane.save()
            messages='Thanks for your advice'

    context = {
        'customer': form,
        'messages':messages
    }
    return render(request, 'user/customarcare.html', context)

@login_required
def smsticket(request):
    form=Smsticketform()
    if request.method == "POST":
        form = Smsticketform(request.POST)

        if form.is_valid():
            sms = form.save(commit=False)
            sms.user=request.user
            sms.save()

    context = {
        'sms': form
    }
    return render(request, 'user/smsticket.html', context)