from django import template

from movie.models import Genre

register = template.Library()


@register.simple_tag
def load_genres():
    return Genre.objects.all()
