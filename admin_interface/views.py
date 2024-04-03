from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages


def movie_list(request):
    banners = MovieBanner.objects.all()
    upmovies = UpcomingMovie.objects.filter().order_by('-release_date')[:4]
    movies = Movie.objects.filter().order_by('-release_date')[:4]
    return render(request, 'home.html', {'movies': movies, 'upmovies': upmovies,'banners':banners})

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
    movies = Portfolio.objects.all()
    return render(request, 'portfolio.html',{'movies':movies})

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
            '3realmsentertainments@gmail.com',  
            ['3realmsentertainments@gmail.com',],  
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will reach you shortly.')
        return render(request, 'contact.html')
    else:
        return HttpResponse('Invalid method')


import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                portfolio = Portfolio.objects.create(
                    title=row['title'],
                    genere=row['genere'],
                    description=row['description'],
                    runtime=row['runtime'],
                    actor=row['actor'],
                    actress=row['actress'],
                    director=row['director'],
                    release_date=row['release_date'],
                    movie_languages=row['movie_languages'],
                    language=row['language'],
                    censor_rating=row['censor_rating'],
                    subtitle_language=row['subtitle_language'],
                    image=row['image']
                )
                if portfolio:
                    return HttpResponse('File uploaded successfully')
    else:
        form = UploadFileForm()
    return render(request, 'upload_excel.html', {'form': form})

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
