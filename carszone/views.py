from django.shortcuts import render
from .models import Teams
from cars.models import Car


# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured = True)
    all_cars = Car.objects.order_by('-created_at')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        # 'search_fields': search_fields
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