from django.db import models

# Create your models here.
class Message(models.Model):
    sent = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=64, default='')
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email  = models.EmailField()
    content = models.CharField(max_length=4096)