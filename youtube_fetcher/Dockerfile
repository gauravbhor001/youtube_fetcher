# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "youtube_fetcher", "worker", "--beat", "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler", "--loglevel=info"]
