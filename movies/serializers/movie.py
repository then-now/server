from rest_framework import serializers
from ..models import Movie, Movie_Ott


class MovieSerializer(serializers.ModelSerializer):
    class Movie_OttSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie_Ott
            fields = (
                "id",
                "ott_id",
                "ott_url",
            )

    movie_movies = Movie_OttSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "poster_path", "movie_movies")
