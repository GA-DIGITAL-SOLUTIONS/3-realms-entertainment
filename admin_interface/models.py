from django.db import models

class Movie(models.Model):
    LANGUAGE_CHOICES = {
        'TELUGU': 'TELUGU',
        'TAMIL': 'TAMIL',
    }
    
    title = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    description = models.TextField()
    runtime = models.CharField(max_length = 20)
    actor = models.CharField(max_length = 100)
    actress = models.CharField(max_length = 100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length = 50,choices = LANGUAGE_CHOICES)
    trailer_link = models.URLField()
    censor_rating = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='movie_images/')
    subtitle_language = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            this = Movie.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Movie, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Movie, self).delete(*args, **kwargs)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='theater_images/',null=True,blank=True)

    def __str__(self):
        return self.name + '---' + self.location

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='showtimes')
    time = models.DateTimeField()
    booking_link = models.URLField()

    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.time.strftime('%Y-%m-%d %H:%M')}"



class UpcomingMovie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='upcoming_movie_images/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = UpcomingMovie.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(UpcomingMovie, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(UpcomingMovie, self).delete(*args, **kwargs)

class Portfolio(models.Model):
    LANGUAGE_CHOICES = {
        'TELUGU': 'TELUGU',
        'TAMIL': 'TAMIL',
    }

    title = models.CharField(max_length=100,null=True,blank=True)
    genere = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    runtime = models.CharField(max_length = 20,null=True,blank=True)
    actor = models.CharField(max_length = 100,null=True,blank=True)
    actress = models.CharField(max_length = 100,null=True,blank=True)
    director = models.CharField(max_length=100,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    movie_languages = models.CharField(max_length = 200,blank=True,null=True)
    language = models.CharField(max_length = 50,choices = LANGUAGE_CHOICES,null=True,blank=True)
    censor_rating = models.CharField(max_length = 10,null=True,blank=True)
    subtitle_language = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='portfolio_images/',null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            this = Portfolio.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(Portfolio, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Portfolio, self).delete(*args, **kwargs)


class MovieBanner(models.Model):
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return self.movie.title
    
    def save(self, *args, **kwargs):
        try:
            this = MovieBanner.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super(MovieBanner, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(MovieBanner, self).delete(*args, **kwargs)



class ContactDetails(models.Model):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.TextField()

