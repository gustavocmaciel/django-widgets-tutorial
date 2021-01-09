from django.shortcuts import render
from django.http import HttpResponse

# Import forms
from django import forms

# Import the User model
##from .models import User

class UserInfoForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "app/index.html", {
                "form": UserInfoForm,
            })
