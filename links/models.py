from django.db import models

# Create your models here.
class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('tiktok', 'TikTok'),
        ('snapchat', 'Snapchat')]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField()