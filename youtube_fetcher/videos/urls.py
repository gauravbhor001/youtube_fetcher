from django.urls import path
from .views import VideoListView, VideoSearchView, dashboard

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/search/', VideoSearchView.as_view(), name='video-search'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('dashboard/', dashboard, name='dashboard'),
]
