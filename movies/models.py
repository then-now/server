from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} : {self.title} {self.poster_path}"


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} : {self.title}"


class Track(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="tracks_movie")
    title = models.CharField(max_length=200)
    track_path = models.CharField(max_length=200)
    genere_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="tracks_genre")

    def __str__(self):
        return f"{self.pk} : {self.movie_id} {self.title} {self.track_path} {self.genere_id}"


class Ott(models.Model):
    movies = models.ManyToManyField(Movie, through="Movie_Ott", related_name="otts")
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} : {self.name}"


class Movie_Ott(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_movies")
    ott_id = models.ForeignKey(Ott, on_delete=models.CASCADE, related_name="movie_otts")
    ott_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} : {self.movie_id} {self.ott_id} {self.ott_url}"
