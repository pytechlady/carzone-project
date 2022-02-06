from django.shortcuts import render

import carszone

# Create your views here.
def home(request):
    return render(request, 'carszone/home.html')

def about(request):
    return render(request, 'carszone/about.html')

def services(request):
    return render(request, 'carszone/services.html')

def contact(request):
    return render(request, 'carszone/contact.html')