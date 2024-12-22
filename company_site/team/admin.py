from django.contrib import admin
from .models import Entity

# Register your models here.
@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'position', 'description')
    list_filter = ('position',)