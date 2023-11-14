from django.contrib import admin
from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru')

class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Country, CountryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rate, RateAdmin)