from django.contrib import admin
from .models import *

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = '3 Realms Entertainment'
    index_title = '3-Realms'

custom_admin_site = CustomAdminSite(name='custom_admin')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date')
    search_fields = ('title', 'director')
    list_filter = ('release_date',)
    date_hierarchy = 'release_date'

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theater', 'time')
    list_filter = ('movie', 'theater', 'time')
    date_hierarchy = 'time'
    
class UpcomingMovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

custom_admin_site.register(Movie, MovieAdmin)
custom_admin_site.register(Theater, TheaterAdmin)
custom_admin_site.register(Showtime, ShowtimeAdmin)
custom_admin_site.register(UpcomingMovie, UpcomingMovieAdmin)
custom_admin_site.register(Portfolio, PortfolioAdmin)