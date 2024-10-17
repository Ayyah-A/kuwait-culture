from django.db import models
from tinymce.models import HTMLField
import datetime

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=100, null=True)
    position_number = models.CharField(max_length=100, null=True)
    date_posted = models.DateField(default=datetime.date.today)
    job_description = HTMLField(null=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ' ' + self.job_title