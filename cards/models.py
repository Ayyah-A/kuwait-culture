from django.db import models

sponsor_choices = (
    ("mohe", "MOHE"),
    ("kuwait university", "Kuwait University"),
    ("civil service", "Civil Service"),
    ("paaet", "PAAET"),
    ("kuwait investment authority", "Kuwait Investment Authority"),
    ("all", "All"),
)

page_choices = (
    ('homepage', 'Homepage'),
    ('home', 'Home'),
    ('students', 'Students'),
    ('rules', 'Rules'),
    ('requirements', 'Requirements'),

)


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=120)
    sponsor = models.CharField(max_length=120, choices=sponsor_choices, null=True)
    page = models.CharField(max_length=120, choices=page_choices, null=True)
    card_link = models.CharField(max_length=500, default='javascript:;')
    image = models.ImageField(upload_to='card_images', null=True, blank=True)
    card_visible = models.BooleanField(default=True)

