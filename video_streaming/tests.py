from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Video

# Create your tests here.

class VideoAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.video = Video.objects.create(user=self.user, name='Test Video', video_url='http://example.com/video.mp4')

    def test_create_video(self):
        data = {'name': 'New Video', 'video_url': 'http://example.com/new_video.mp4'}
        response = self.client.post('/api/videos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_video(self):
        response = self.client.get(f'/api/videos/{self.video.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
