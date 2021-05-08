from django.views.generic import ListView, DetailView

from .models import Movie


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 5
    ordering = '-title'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'


class MoviesByGenre(ListView):
    model = Movie
    paginate_by = 5
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        return Movie.objects.filter(genres__slug=self.kwargs.get('slug')).order_by('-title')
