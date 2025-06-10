from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length= 150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class MediaType(models.Model): 
    media_type_choices = [
    ('Movie', 'Movie'),
    ('TV Show', 'TV Show'),
    ('Series', 'Series'),
    ('Documentary', 'Documentary'),
    ('Short Film', 'Short Film'),
    ('Film', 'Film'),
]
    
    media_type = models.CharField(choices=media_type_choices, max_length=50, null=True, blank=True)
    genre = models.CharField(max_length = 50, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title