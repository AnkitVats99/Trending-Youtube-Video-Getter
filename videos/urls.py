
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('fetch_video_data/', views.fetch_youtube_videos, name="fetch_youtube_videos"),
]