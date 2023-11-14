from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('create/', views.CreateMovie.as_view(), name='create'),
    path('edit/<int:movie_id>/', views.EditMovie.as_view(), name='edit'),
    path('detail/<int:movie_id>/', views.MovieDetailView.as_view(), name='detail'),
    path('delete/<int:movie_id>/', views.DeleteFilmView.as_view(), name='delete'),
    path('rate/', views.RateView.as_view(), name='rate'),
]