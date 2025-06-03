from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    # This is the POST method for creating a new movie
    def create(self, validated_data):
        # validated data is passed to create method of Movie model
        return Movie.objects.create(**validated_data) # the ** operator unpacks the dictionary
    
