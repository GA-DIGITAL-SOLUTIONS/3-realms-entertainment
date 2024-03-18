from django import forms
from .models import Theater, Movie, Showtime, Booking

class TheaterForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = ['name', 'location']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'trailer_link', 'image', 'theaters']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
class ShowtimeForm(forms.ModelForm):
    class Meta:
        model = Showtime
        fields = ['theater', 'time']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['showtime', 'user_name', 'num_tickets']
