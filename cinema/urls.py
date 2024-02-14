from django.urls import path
from .views import movies_list, movie_detail

urlpatterns = [
    path("api/cinema/movies/", movies_list, name="movies_list"),
    path("api/cinema/movies/<pk>/", movie_detail, name="movie_detail"),
]
