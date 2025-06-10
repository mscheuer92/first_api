from django.urls import path
from watchlist_app.api.views import MediaTypeDetailAPIView, MediaTypeListCreateAPIView, MediaTypeTitleFilterAPIView, StreamPlatformList

urlpatterns = [
    path('list/',MediaTypeListCreateAPIView.as_view(), name='media-list'),
    path('<int:pk>/', MediaTypeDetailAPIView.as_view(), name='media-detail'),
    path('title/<str:title>/', MediaTypeTitleFilterAPIView.as_view(), name='media-title-filter'),
    path('platforms/', StreamPlatformList.as_view(), name='platform-list'),
]
