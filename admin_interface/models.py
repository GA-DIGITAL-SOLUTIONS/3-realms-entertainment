from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100)
    star_cast = models.TextField()
    release_date = models.DateField()
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
