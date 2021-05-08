from django.urls import path

from .views import MovieList, MoviesByGenre, MovieDetail

app_name = 'movie'
urlpatterns = [
    path('<slug:slug>', MoviesByGenre.as_view(), name='movie_by_genre'),
    path('<slug:slug>/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('', MovieList.as_view(), name='movie'),
]
