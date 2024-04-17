from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, blank=True)
    page_body = HTMLField( blank=True)
    page = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=100)

