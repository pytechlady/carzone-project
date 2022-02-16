from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        
        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone_number=phone_number,
            message=message
            )
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait for our response.')
                return redirect('/cars/'+car_id)
        

        send_mail(
            'New Car Inquiry',
            'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel to view message.',
            'admin@carzone.com',
            ['solveit37@gmail.com'],
            fail_silently=False,
        )
        
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly')
        return redirect('/cars/'+car_id)