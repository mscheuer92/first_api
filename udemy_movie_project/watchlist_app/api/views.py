from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import MediaType, StreamPlatform
from watchlist_app.api.serializers import MediaSerializer, StreamPlatformSerializer


class StreamPlatformList(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=422)


class MediaTypeListCreateAPIView(APIView):
    def get(self, request):
        media = MediaType.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=422)

class MediaTypeDetailAPIView(APIView):
    def get(self, request, pk):
        media = MediaType.objects.get(pk=pk)
        serializer = MediaSerializer(media)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        try:
            media = MediaType.objects.get(pk=pk)
            serializer = MediaSerializer(media, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=422)
        except MediaType.DoesNotExist:
            return Response({"error": "Media not found"}, status=404)
            
    def delete(self, request, pk):
        media = MediaType.objects.get(pk=pk)
        media.delete()
        return Response({"message": "Media deleted successfully"}, status=204)    

class MediaTypeTitleFilterAPIView(APIView):
    def get(self, request, title):
        try:
            media = MediaType.objects.get(title=title)
            serializer = MediaSerializer(media)
            return Response(serializer.data)
        except MediaType.DoesNotExist:
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