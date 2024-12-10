from django.contrib import admin
from models import *

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sent', 'company', 'name', 'surname', 'email', 'content')
    list_filter = ('sent', 'company')