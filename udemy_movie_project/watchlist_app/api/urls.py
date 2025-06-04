from django.urls import path
from watchlist_app.api.views import movie_list, movie_detail, movie_title

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>/', movie_detail, name='movie-detail'),
    path('title/<str:title>/', movie_title, name='movie-title-filter'),
]
