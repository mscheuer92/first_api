from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create fucntion or class-based views here.
# Using function based view to extract all active movies.
def movie_list(request):
    # Here we extract everything by creating a queryset. 
    # This means selecting all avaliable objects from the Movie model 
    # and using them one by one or in a list.
    
    # Query set
    movies = Movie.objects.all()
    # Need to be returned as json.
    data = {'movies': list(movies.values())}

    return JsonResponse(data)

def movie_detail(request, pk):
    #extract movie by id
    movie_detail = Movie.objects.get(pk=pk)
    # data = {"description": movie_detail.description}
    data = {
        "title": movie_detail.title,
        "description": movie_detail.description,
        "active": movie_detail.active
    }
    return JsonResponse(data)
