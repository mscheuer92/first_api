from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail, movie_title
from watchlist_app.api.views import MovieListCreateAPIView, MovieDetailAPIView

urlpatterns = [
    path('list/', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('title/<str:title>/', MovieDetailAPIView.as_view(), name='movie-title-filter'),
]
