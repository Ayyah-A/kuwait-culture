from django.db import models
from ckeditor.fields import RichTextField
import datetime

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=500)
    post_date = models.DateField(default=datetime.date.today)
    body = RichTextField(blank=True)
    image = models.FileField(upload_to='announcement_imgs/', blank=True)
    document_file = models.FileField(upload_to='announcement_docs/', blank=True)
    publish = models.BooleanField(default=True)
    homepage_headline = models.BooleanField()
    important_announce = models.BooleanField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
