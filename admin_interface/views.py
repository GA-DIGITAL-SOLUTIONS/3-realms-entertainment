from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Theater, Showtime

def movie_list(request):
    locations = Theater.objects.values_list('location', flat=True).distinct()
    location = request.GET.get('location')
    if location:
        movies = Movie.objects.filter(showtimes__theater__location__icontains=location).distinct()
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies, 'locations': locations, 'selected_location': location})

def movie_synopsis(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        movie = None

    theaters = Theater.objects.all()

    location_filter = request.GET.get('location')
    if location_filter:
        theaters = theaters.filter(location=location_filter)

    context = {
        'movie': movie,
        'theaters': theaters,
    }
    return render(request, 'movie_synopsis.html', context)