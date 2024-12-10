from django.db import models

# Create your models here.
class Entity(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)