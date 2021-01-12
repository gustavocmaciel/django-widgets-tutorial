from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserInfoForm


def index(request):
    return render(request, "app/index.html", {
        "form": UserInfoForm,
    })

