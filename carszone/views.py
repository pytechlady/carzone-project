from django.shortcuts import render
from .models import Teams

import carszone

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'carszone/home.html', data)

def about(request):
    teams = Teams.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'carszone/about.html', data)

def services(request):
    return render(request, 'carszone/services.html')

def contact(request):
    return render(request, 'carszone/contact.html')