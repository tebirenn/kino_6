from django.db import models
import uuid

from authe.models import User

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'posters/{new_file_name}'

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Movie(models.Model):
    poster = models.ImageField(blank=True, null=True, upload_to=uniq_name_upload)
    trailer_url = models.URLField()
    title_ru = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    description = models.TextField()
    publish_year = models.IntegerField()
    timing = models.IntegerField()
    premier_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_orig
    
    def to_json(self):
        return {
            'poster': self.poster,
            'trailer_url': self.trailer_url,
            'title_ru': self.title_ru,
            'title_orig': self.title_orig,
            'description': self.description,
            'publish_year': self.publish_year,
            'premier_date': self.premier_date,
            'country': self.country,
            'genre': self.genre,
            'director': self.director,
            'timing': self.timing,
        }


class Rate(models.Model):
    count = models.IntegerField(null=False)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
