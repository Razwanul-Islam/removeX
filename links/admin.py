from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SocialMediaLink, MenuItem

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(ModelAdmin):
    list_display = ('platform', 'url')
    search_fields = ('platform', 'url')
    list_filter = ('platform',)
    ordering = ('platform',)

@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ('name', 'url', 'order')
    search_fields = ('name', 'url')
    ordering = ('order',)
# Register your models here.
