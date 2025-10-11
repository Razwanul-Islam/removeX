from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SocialMediaLink

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(ModelAdmin):
    list_display = ('platform', 'url')
    search_fields = ('platform', 'url')
    list_filter = ('platform',)
    ordering = ('platform',)
# Register your models here.
