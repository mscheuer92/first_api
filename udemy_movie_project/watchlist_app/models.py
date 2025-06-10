from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length= 150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class MediaType(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(default=True, max_length=200)
    active = models.BooleanField(default=True) # active = released
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title