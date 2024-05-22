from celery import shared_task
import requests
from .models import Video
from django.conf import settings

API_KEYS = ['YOUR_API_KEY_1', 'YOUR_API_KEY_2']  # Add multiple keys
current_key_index = 0

@shared_task
def fetch_youtube_videos():
    global current_key_index
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    api_key = API_KEYS[current_key_index]
    params = {
        'part': 'snippet',
        'q': 'YOUR_SEARCH_QUERY',
        'type': 'video',
        'order': 'date',
        'key': api_key
    }
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        videos = response.json().get('items', [])
        for video in videos:
            video_data = video['snippet']
            video_id = video['id']['videoId']
            Video.objects.update_or_create(
                video_id=video_id,
                defaults={
                    'title': video_data['title'],
                    'description': video_data['description'],
                    'published_at': video_data['publishedAt'],
                    'thumbnail_url': video_data['thumbnails']['default']['url']
                }
            )
    elif response.status_code == 403:  # Quota exhausted
        current_key_index = (current_key_index + 1) % len(API_KEYS)
