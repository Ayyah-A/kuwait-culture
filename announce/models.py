from django.db import models
from tinymce.models import HTMLField
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=500)
    post_date = models.DateField(default=datetime.date.today)
    body = HTMLField(blank=True)
    image = models.ImageField(upload_to='announcements/imgs/', blank=True, null=True)
    file = models.FileField(upload_to='announcements/docs/', blank=True, null=True)
    publish = models.BooleanField(default=True)
    important = models.BooleanField()
    homepage_headline = models.BooleanField()

    def __str__(self):
        return str(self.id) + ' ' + self.title
