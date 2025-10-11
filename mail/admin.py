from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldAdmin
from .models import ContactMessage, ContactUsReceiver

@admin.register(ContactMessage)
class ContactMessageAdmin(UnfoldAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(ContactUsReceiver)
class ContactUsReceiverAdmin(UnfoldAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    ordering = ('email',)
