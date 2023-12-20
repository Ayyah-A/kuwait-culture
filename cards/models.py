from django.db import models

sponsor_choices = (
    ("mohe", "MOHE"),
    ("kuwait university", "Kuwait University"),
    ("civil service", "Civil Service"),
    ("paaet", "PAAET"),
    ("kuwait investment authority", "Kuwait Investment Authority"),
)

page_choices = (
    ('home', 'Home'),
    ('rules', 'Rules'),
    ('requirements', 'Requirements'),
)


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=120)
    sponsor = models.CharField(max_length=120, choices=sponsor_choices, null=True)
    page = models.CharField(max_length=120, choices=page_choices, null=True)
    card_link = models.CharField(max_length=500, default='javascript:;')
    card_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.sponsor + "-" + self.page + "-" + self.title
