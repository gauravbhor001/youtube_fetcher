from django.shortcuts import render
from rest_framework import generics, filters
from .models import Video
from .serializers import VideoSerializer

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by('-published_at')
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class VideoSearchView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


def dashboard(request):
    query = request.GET.get('q')
    videos = Video.objects.all()

    if query:
        videos = videos.filter(title__icontains=query) | videos.filter(description__icontains=query)

    videos = videos.order_by('-published_datetime')

    return render(request, 'videos/dashboard.html', {'videos': videos})
