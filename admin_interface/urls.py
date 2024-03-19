from django.urls import path
from . import views
from .admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_synopsis, name='movie_synopsis'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('up-movies', views.up_movies, name='up-movies'),
    path('latest-movies', views.latest_movies, name='latest_movies'),
    path('sendmail', views.sendmail, name='sendmail'),
    
]