from django.urls import path
from .views import VideoListCreateAPIView, VideoRetrieveUpdateDestroyAPIView

app_name = 'video_streaming'

urlpatterns = [
    path('api/videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('api/videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-detail'),
]
