from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages


def movie_list(request):
    banners = MovieBanner.objects.all()
    upmovies = UpcomingMovie.objects.filter().order_by('-release_date')[:4]
    movies = Movie.objects.filter().order_by('-release_date')[:4]
    contact_info = ContactDetails.objects.all()[0]
    return render(request, 'home.html', {'movies': movies, 'upmovies': upmovies,'banners':banners,'contact_info': contact_info})

def latest_movies(request):
    movies = Movie.objects.all()
    contact_info = ContactDetails.objects.all()[0]
    return render(request, 'latest-movies.html', {'movies': movies,'contact_info': contact_info})

def movie_synopsis(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        movie = None
    contact_info = ContactDetails.objects.all()[0]
    locations = Theater.objects.values_list('location', flat=True).distinct()
    
    theaters = Theater.objects.filter(showtimes__movie=movie).distinct()

    context = {
        'movie': movie,
        'theaters': theaters,
        'locations': locations,
        'contact_info': contact_info
    }
    return render(request, 'movie_synopsis.html', context)


def portfolio_detail(request, movie_id):
    try:
        movie = Portfolio.objects.get(pk=movie_id)
    except Portfolio.DoesNotExist:
        movie = None
    contact_info = ContactDetails.objects.all()[0]
    context = {
        'movie': movie,
        'contact_info': contact_info
    }
    return render(request, 'portfolio-details.html', context)

def contact(request):
    contact_info = ContactDetails.objects.all()[0]
    return render(request, 'contact.html',{'contact_info': contact_info})

def portfolio(request):
    contact_info = ContactDetails.objects.all()[0]
    movies = Portfolio.objects.all().order_by('-release_date')
    return render(request, 'portfolio.html',{'movies':movies,'contact_info': contact_info})

def about(request):
    contact_info = ContactDetails.objects.all()[0]
    return render(request, 'about.html',{'contact_info': contact_info})


def up_movies(request):
    contact_info = ContactDetails.objects.all()[0]
    upmovies = UpcomingMovie.objects.all()
    return render(request, 'upcoming-movies.html', {'upmovies': upmovies,'contact_info': contact_info})


def sendmail(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        notification = f'Name: {name}\nEmail: {email}\nContact: {phone}\nMessage: {message}'

        send_mail(
            'New Enquiry',
            notification,
            '3realmsentertainments@gmail.com',  
            ['3realmsentertainments@gmail.com',],  
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will reach you shortly.')
        return render(request, 'contact.html')
    else:
        return HttpResponse('Invalid method')