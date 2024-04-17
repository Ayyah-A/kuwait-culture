from django.db import models


# Create your models here.
class Document(models.Model):
    doc_name = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to="documents", null=True, blank=False)
    published = models.BooleanField(default=True)
    important_doc = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.doc_name