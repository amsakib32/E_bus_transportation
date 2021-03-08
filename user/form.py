from django import forms
from .models import Profile,Customercare,Smsticket
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['Date_Of_Birth','n_id','contact','address']


class UserCreationForm(UserCreationForm):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Customerform(forms.ModelForm):
    class Meta:
        model=Customercare
        fields=['Options','Complain']

class Smsticketform(forms.ModelForm):
    class Meta:
        model=Smsticket
        fields=['Phone_no','Ticket_no']