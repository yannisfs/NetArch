from django.db import models

# Create your models here.
class Offer(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    price_range = models.CharField(max_length=32)
    available = models.BooleanField(default=True)