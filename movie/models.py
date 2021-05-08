from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse, reverse_lazy


class Director_by(models.Model):
    name = models.CharField(max_length=60, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='Название', db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    ordering = ['title']

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def get_absolute_url(self):
        return reverse_lazy('movie:movie_by_genre', args=[self.slug])

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    directors = models.ManyToManyField(Director_by, verbose_name='Создатель')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='movie/%Y/%m/%d', verbose_name='Картинка')
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('movie:movie_detail', args=[self.slug, self.id])

    def __str__(self):
        return self.title
