from django.urls import path
from watchlist_app.views import movie_list

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
]
