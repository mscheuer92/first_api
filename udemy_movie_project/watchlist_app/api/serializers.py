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
    
    # This is the PUT menthod for updating an existing movie
    def update(self, instance, validated_data):
        # instance is the movie object to be updated, validated_data is the new data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # Field level validation
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('The title must be at least 2 characters long.')
        else:
            return value
    
    # object level validation
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("The title and description cannot be the same.")