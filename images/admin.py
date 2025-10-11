from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import HeaderImage, GalleryImage

@admin.register(HeaderImage)
class HeaderImageAdmin(ModelAdmin):
    list_display = ('type', 'image')
    search_fields = ('type',)
    list_filter = ('type',)
    ordering = ('type',)

@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ('id', 'alt_text', 'image')
    search_fields = ('alt_text',)
    ordering = ('id',)
# Register your models here.
