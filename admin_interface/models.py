from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    description = models.TextField()
    runtime = models.DecimalField(max_digits=10,decimal_places=2)
    actor = models.CharField(max_length = 100)
    actress = models.CharField(max_length = 100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length = 50)
    trailer_link = models.URLField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='showtimes')
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.time.strftime('%Y-%m-%d %H:%M')}"
