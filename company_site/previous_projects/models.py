from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=4096)
    client = models.CharField(max_length=128, blank=True)
    timeframe = models.CharField(max_length=128, blank=True)