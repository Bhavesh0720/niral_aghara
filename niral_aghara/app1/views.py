from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *

# Create your views here.
def index(request):    
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        if not phone.isdigit():
            messages.warning(request, "Phone Number Must Be Digit!")
        else:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            send_mail(
                subject=f"New Contact Form: {subject}",
                message=message,
                from_email=email,
                recipient_list=['your_email@gmail.com'],  # where you receive messages
                fail_silently=False,
            )    

            messages.success(request, "Message Sent Successfully!")
        
        return redirect('contact')

    return render(request, 'contact.html')


def cources(request):
    cources = Cources.objects.all()
    return render(request, 'cources.html', {
        'cources':cources
    })


def disclaimer(request):
    return render(request, 'disclaimer.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms(request):
    return render(request, 'terms.html')


def youtube(request):
    playlists = PlayLists.objects.all()
    popular_videos = MostPopular.objects.all()
    return render(request, 'youtube.html', {
        'playlists':playlists,
        'popular_videos':popular_videos
    })