from django.shortcuts import get_object_or_404
from .models import Movie, Genre
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.movie import MovieSerializer
from .serializers.genre import GenreListSerializer

# Create your views here.
@api_view(["GET"])
def genre_list(request, genre_pk):
    genres = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreListSerializer(genres)
    return Response(serializer.data)


@api_view(["GET"])
def movie_detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
