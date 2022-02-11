from django.shortcuts import render
from .models import Teams
from cars.models import Car


# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_at')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars
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