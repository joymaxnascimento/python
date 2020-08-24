from django.shortcuts import render
import os
from pathlib import Path

from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'principal/index.html')
