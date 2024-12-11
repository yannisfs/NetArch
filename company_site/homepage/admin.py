from django.contrib import admin
from .models import Update

# Register your models here.
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text', 'author', 'date')