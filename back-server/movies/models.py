from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.IntegerField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='genres')

class Actor(models.Model):
    actor_pk = models.AutoField(primary_key=True)
    gender = models.IntegerField()
    name = models.CharField(max_length=50)
    popularity = models.IntegerField()
    profile_path = models.TextField(null=True)
    character = models.CharField(max_length=100)
    movie_id = models.IntegerField()
