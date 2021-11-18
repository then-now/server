from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Movie, Ott
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.movie import MovieSerializer, MovieListSerializer
from movies import serializers

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
