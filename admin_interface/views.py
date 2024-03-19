from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def movie_list(request):
    upmovies = UpcomingMovie.objects.all()
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies, 'upmovies': upmovies})

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
    movies = Movie.objects.all()
    return render(request, 'portfolio.html',{'movies': movies})

def about(request):
    return render(request, 'about.html')


