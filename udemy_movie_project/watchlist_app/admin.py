from django.contrib import admin
from watchlist_app.models import MediaType, StreamPlatform

# Register your models here.

admin.site.register(MediaType)
admin.site.register(StreamPlatform)