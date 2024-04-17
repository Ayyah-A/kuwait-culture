from django.db import models

department_choices = (
    ('cultural_counselor_office', 'Cultural Counselor’s Office'),
    ('cultural_attache_office', 'Cultural Attache’s Office'),
    ('accounting', 'Accounting'),
    ('administration', 'Administration'),
    ('placement', 'Placement'),
    ('program_eval', 'Program Evaluation'),
    ('graduate', 'Graduate'),
    ('undergraduate', 'Undergraduate'),
    ('translation', 'Translation'),
    ('information_technology', 'Information Technology'),
)
# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200, choices=department_choices)
    email = models.EmailField()
    work_phone = models.CharField(max_length=200)
    info_page = models.CharField(max_length=500, null=True, blank=True)
    emp_photo = models.ImageField(upload_to='diplomat_images/', blank=True, null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name