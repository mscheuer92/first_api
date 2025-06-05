from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

class MovieListCreateAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=422)

class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=422)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
            
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({"message": "Movie deleted successfully"}, status=204)    

class MovieTitleFilterAPIView(APIView):
    def get(self, request, title):
        try:
            movie = Movie.objects.get(title=title)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"error": "Title not found"}, status=404)


#FUNCTION BASED VIEWS
# # return a list of all movies
# @api_view(['GET','POST'])
# def movie_list(request):
#     match request.method:
#         case 'GET':
#             movie = Movie.objects.all()
#             # Use serializer
#             serializer = MovieSerializer(movie, many=True)
#             return Response(serializer.data, status=200)
#         case 'POST':
#             serializer = MovieSerializer(data=request.data) # get data from user request
#             if serializer.is_valid(): # data is considered valid if it's in the correct format
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             else:
#                 return Response(serializer.errors, status=422)

# # return a single movie
# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#         match request.method:
#             case "GET":
#                 serializer = MovieSerializer(movie)
#                 return Response(serializer.data)
#             case "PUT":
#                 movie = Movie.objects.get(pk=pk)
#                 serializer = MovieSerializer(movie, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=200)
#                 else:
#                     return Response(serializer.errors, status=422)
#             case "DELETE":
#                 movie.delete()
#                 return Response(status=204)
#     except Movie.DoesNotExist:
#         return Response({"error": "Movie not found"}, status=404)

# # filter movies by title
# @api_view()
# def movie_title(request, title):
#     try:
#         movie = Movie.objects.get(title=title)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     except Movie.DoesNotExist:
#         return Response({"error": "Title not found"}, status=404)