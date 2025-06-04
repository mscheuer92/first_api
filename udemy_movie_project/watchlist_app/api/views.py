from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

# return a list of all movies
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        # Use serializer
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)


# return a single movie
@api_view(['GET','POST'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# filter movies by title
@api_view()
def movie_title(request, title):
    movie = Movie.objects.get(title=title)
    serializer = MovieSerializer()
    return Response(serializer.data)