from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.IntegerField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    genres = models.TextField()