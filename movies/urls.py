from django.urls import path
from . import views

urlpatterns = [
    path("genre/<int:genre_pk>/", views.genre_list),
    path("movie/<int:movie_pk>/", views.movie_detail),
]
