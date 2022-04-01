from django.db import models

# Create your models here.

#footer previous events
class PreviousEvent(models.Model):
    image = models.ImageField(upload_to='prevEventsPhotos/', default=None)
    link = models.URLField()
    year = models.IntegerField()