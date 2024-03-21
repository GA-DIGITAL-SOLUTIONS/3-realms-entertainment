from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse


def movie_list(request):
    upmovies = UpcomingMovie.objects.filter().order_by('-release_date')[:4]
    movies = Movie.objects.filter().order_by('-release_date')[:4]
    return render(request, 'home.html', {'movies': movies, 'upmovies': upmovies})

def latest_movies(request):
    movies = Movie.objects.all()
    return render(request, 'latest-movies.html', {'movies': movies})

def movie_synopsis(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        movie = None
    locations = Theater.objects.values_list('location', flat=True).distinct()
    
    theaters = Theater.objects.filter(showtimes__movie=movie).distinct()
    location_filter = request.GET.get('location')
    if location_filter:
        theaters = theaters.filter(location=location_filter)

    context = {
        'movie': movie,
        'theaters': theaters,
        'locations': locations,
    }
    return render(request, 'movie_synopsis.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    all_movies = Portfolio.objects.all()
    telugu_movies = Portfolio.objects.filter(language = 'TELUGU')
    tamil_movies = Portfolio.objects.filter(language = 'TAMIL')
    return render(request, 'portfolio.html',{'all_movies':all_movies,'telugu_movies': telugu_movies,'tamil_movies': tamil_movies})

def about(request):
    return render(request, 'about.html')


def about(request):
    return render(request, 'about.html')

def up_movies(request):
    upmovies = UpcomingMovie.objects.all()
    return render(request, 'upcoming-movies.html', {'upmovies': upmovies})


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
            '',  
            ['hemachandra521@gmail.com'],  
            fail_silently=False,
        )

        return HttpResponse('Email sent successfully')  
    else:
        return HttpResponse('Invalid method')  

