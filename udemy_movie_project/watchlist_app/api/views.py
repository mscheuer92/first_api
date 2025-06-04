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
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data) # get data from user request
        if serializer.is_valid(): # data is considered valid if it's in the correct format
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)

# return a single movie
@api_view(['GET','PUT','DELETE'])
def movie_detail(request, pk):
    match request.method:
        case "GET":
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        case "PUT":
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        case "DELETE":
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=204)
            
     

# filter movies by title
@api_view()
def movie_title(request, title):
    movie = Movie.objects.get(title=title)
    serializer = MovieSerializer()
    return Response(serializer.data)