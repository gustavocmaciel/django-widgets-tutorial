from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.forms import ModelForm, TextInput, EmailInput 

from .models import User

# Form to get the user info
class UserInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "app/index.html", {
                "form": UserInfoForm,
            })
