from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from authe.models import User
from .forms import *
from .models import *

# Create your views here.
class Home(View):
    def get(self, request):
        movies = Movie.objects.all()

        context = {
            'title': 'Все фильмы',
            'movies': movies,
        }

        return render(request, 'movies/index.html', context=context)
    
class CreateMovie(View):
    def get(self, request):
        form = MovieCreationForm()

        context = {
            'title': 'Создать фильм',
            'form': form
        }

        return render(request, 'movies/create.html', context=context)
    
    def post(self, request):
        form = MovieCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('movies:index'))
        else:
            context = {
                'title': 'Создать фильм',
                'form': form,
                'error': 1,
            }

            return render(request, 'movies/create.html', context=context)
        

class EditMovie(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        form = MovieCreationForm(movie.to_json())

        context = {
            'title': 'Редактировать фильм',
            'form': form,
            'movie': movie,
        }

        return render(request, 'movies/edit.html', context=context)
    
    def post(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        form = MovieCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                movie.poster = request.FILES['poster']
            
            movie.title_ru = request.POST['title_ru']
            movie.title_orig = request.POST['title_orig']
            movie.trailer_url = request.POST['trailer_url']
            movie.description = request.POST['description']
            movie.publish_year = request.POST['publish_year']
            movie.timing = request.POST['timing']
            movie.country = Country.objects.get(id=request.POST['country'])
            movie.genre = Genre.objects.get(id=request.POST['genre'])
            movie.director = Director.objects.get(id=request.POST['director'])
            
            movie.save()
            return redirect(reverse_lazy('movies:index'))
        else:
            context = {
                'title': 'Редактировать фильм',
                'form': form,
                'movie': movie,
                'error': 1,
            }
            return render(request, 'movies/edit.html', context=context)

def avg_rate(rates):
    res = 0

    for rate in rates:
        res += rate.count
    
    return f'{res / len(rates):.1f}'

class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        rates = Rate.objects.filter(movie_id=movie_id)

        context = {
            'title': movie.title_ru,
            'movie': movie,
            'rates': rates,
            'avg_rate': avg_rate(rates),
        }

        return render(request, 'movies/detail.html', context=context)
    
class DeleteFilmView(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        movie.delete()

        return redirect(reverse_lazy('movies:index'))


class RateView(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
            
        movie_id = data.get('movie_id')
        text = data.get('text')
        count = data.get('count')
        user_id = data.get('user_id')

        movie = Movie.objects.get(id=movie_id)
        user = User.objects.get(id=user_id)
        
        rate = Rate.objects.create(
            count=count,
            text=text,
            author=user,
            movie=movie
        )        
        rate.save()
        
        return HttpResponse({'data': 'success'})
