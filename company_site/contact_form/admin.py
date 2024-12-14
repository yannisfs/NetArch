from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'surname', 'email', 'content','requested_quote', 'get_related_offer_slug', 'sent')
    readonly_fields = ('sent',)
    list_filter = ('sent', 'company', 'surname', 'requested_quote')

    def get_related_offer_slug(self, obj):
        return obj.offer.slug if obj.offer else None
    get_related_offer_slug.short_description = 'Offer Slug'