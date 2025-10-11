from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold import admin as unfold_admin
from .models import SectionTitle,HeaderText, AboutCard, ServiceCard, ProcessCard, ContactInfo, FooterText
# Register your models here.

@admin.register(SectionTitle)
class SectionTitleAdmin(ModelAdmin):
    list_display = ('section', 'title')
    search_fields = ('section', 'title')
    list_filter = ('section',)
    ordering = ('section',)

@admin.register(HeaderText)
class HeaderTextAdmin(ModelAdmin):
    list_display = ('type', 'content')
    search_fields = ('type', 'content')
    list_filter = ('type',)
    ordering = ('type',)

@admin.register(AboutCard)
class AboutCardAdmin(ModelAdmin):
    list_display = ('curcle_icon', 'title', 'description')
    search_fields = ('title', 'description')
    ordering = ('title',)

@admin.register(ServiceCard)
class ServiceCardAdmin(ModelAdmin):
    list_display = ('title', 'subtitle', 'list_of_services')
    search_fields = ('title', 'subtitle', 'list_of_services')
    ordering = ('title',)

@admin.register(ProcessCard)
class ProcessCardAdmin(ModelAdmin):
    list_display = ('step_number', 'title', 'description')
    search_fields = ('title', 'description')
    ordering = ('step_number',)

@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin):
    list_display = ('type', 'content')
    search_fields = ('type', 'content')
    list_filter = ('type',)
    ordering = ('type',)

@admin.register(FooterText)
class FooterTextAdmin(ModelAdmin):
    list_display = ('type', 'content')
    search_fields = ('type', 'content')
    list_filter = ('type',)
    ordering = ('type',)