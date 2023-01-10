from datetime import timedelta

from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    speaker_name = models.CharField(max_length=40)
    speakers_avatar = models.ImageField(upload_to="app/images", default="")
    date_select = models.DateField(default=timezone.now)
    duration = models.DurationField(default=timedelta)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    class Meta:
        ordering = ['speaker_name', 'date_select', 'duration']

    def __str__(self):
        return self.title + " , " + self.speaker_name
