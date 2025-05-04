from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    cca2 = models.CharField(max_length=10)
    capital = models.CharField(max_length=255, blank=True, null=True)
    population = models.BigIntegerField(default=0)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    languages = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name