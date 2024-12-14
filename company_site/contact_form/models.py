from django.db import models
from pricing.models import Offer

# Create your models here.
class Message(models.Model):
    sent = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=64,blank=True)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email  = models.EmailField()
    content = models.CharField(max_length=4096)
    requested_quote = models.BooleanField(default=False)  # Tracks if this was a "Get Quote" request
    offer = models.ForeignKey(Offer, null=True, blank=True, on_delete=models.SET_NULL)