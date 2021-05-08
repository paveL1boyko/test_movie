from django.contrib import admin

from .models import Director_by, Movie, Genre


@admin.register(Director_by)
class DirectorByAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'slug')
    list_display_links = ('name', 'surname', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ['name', 'surname']}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ['title', 'genres']}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ['title']}
