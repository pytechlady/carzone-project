from django.shortcuts import render, redirect
from .models import Teams
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + ', Email: ' + email + ', Phone: ' + phone + ', Message: ' + message
        
        send_mail(
        email_subject,
        message_body,
        'admin@carzone.com',
        ['solveit37@gmail.com'],
        fail_silently=False,
        )
        messages.success(request, "Thank you for contacting us. We will get back shortly.")   
        return redirect('contact')
    return render(request, 'carszone/contact.html')
