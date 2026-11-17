
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    courses = models.TextField(blank=True)
    courses_offered = models.TextField(blank=True)

    fees = models.CharField(max_length=100, blank=True)
    kcet_fee = models.CharField(max_length=100, blank=True)
    comedk_fee = models.CharField(max_length=100, blank=True)
    management_fee = models.CharField(max_length=100, blank=True)

    kcet_cutoff = models.CharField(max_length=200, blank=True)
    comedk_cutoff = models.CharField(max_length=200, blank=True)

    average_package = models.CharField(max_length=100, blank=True)
    highest_package = models.CharField(max_length=100, blank=True)

    established_year = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=30, blank=True)

    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
