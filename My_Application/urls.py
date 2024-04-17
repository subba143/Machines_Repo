"""My_Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from video_streaming.views import VideoListCreateAPIView, VideoRetrieveUpdateDestroyAPIView
from oee_calculation.views import MachineListCreateAPIView, MachineRetrieveUpdateDestroyAPIView, ProductionLogListCreateAPIView, ProductionLogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('api/videos/<int:pk>/', VideoRetrieveUpdateDestroyAPIView.as_view(), name='video-detail'),

    path('api/machines/', MachineListCreateAPIView.as_view(), name='machine-list-create'),
    path('api/machines/<int:pk>/', MachineRetrieveUpdateDestroyAPIView.as_view(), name='machine-detail'),
    path('api/production-logs/', ProductionLogListCreateAPIView.as_view(), name='production-log-list-create'),
    path('api/production-logs/<int:pk>/', ProductionLogRetrieveUpdateDestroyAPIView.as_view(), name='production-log-detail'),
]




