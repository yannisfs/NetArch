from django.contrib import admin
from .models import Offer

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'description', 'price_range', 'available')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'available')
    