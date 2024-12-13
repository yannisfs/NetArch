from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'surname', 'email', 'content', 'sent')
    readonly_fields = ('sent',)
    list_filter = ('sent', 'company', 'surname')