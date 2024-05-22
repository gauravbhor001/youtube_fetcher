from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()


    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['published_at']),
        ]
