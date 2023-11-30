from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.EmailField()
    work_phone = models.CharField(max_length=200)
    publish = models.BooleanField()

    def __str__(self):
        return self.first_name + " " + self.last_name
