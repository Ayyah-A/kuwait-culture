from django.db import models

department_choices = (
    ('cultural counselor’s office', 'Cultural Counselor’s Office'),
    ('cultural attache’s office', 'Cultural Attache’s Office'),
    ('accounting', 'Accounting'),
    ('administration', 'Administration'),
    ('authentication', 'Authentication'),
    ('graduate', 'Graduate'),
    ('undergraduate', 'Undergraduate'),
    ('translation', 'Translation'),
    ('information technology', 'Information Technology'),
)
# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200, choices=department_choices)
    email = models.EmailField()
    work_phone = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
