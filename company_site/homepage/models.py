from django.db import models

# Create your models here.
class Update(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=2048)
    author = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True, editable=True)
    show = models.BooleanField(default=True)
