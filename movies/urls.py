from django.urls import path
from . import views

urlpatterns = [
    path("genre/", views.genre_list),
    path("movie/<int:movie_pk>/", views.movie_detail),
]
