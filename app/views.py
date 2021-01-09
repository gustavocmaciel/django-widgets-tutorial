from django.shortcuts import render
from django.http import HttpResponse

# Import forms
from django import forms
from django.forms import ModelForm, TextInput, EmailInput 

# Import the User model
##from .models import User

class UserInfoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "app/index.html", {
                "form": UserInfoForm,
            })
