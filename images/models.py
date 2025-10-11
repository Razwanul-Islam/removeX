from django.db import models
import os
from django.conf import settings

# Create your models here.

class HeaderImage(models.Model):
    TYPE = [
        ('hero-image', 'Hero Image'),
    ]
    type = models.CharField(max_length=20, choices=TYPE, unique=True)
    image = models.ImageField(upload_to='header_images/')

    def __str__(self):
        return f"{self.type}"
    
    def save(self, *args, **kwargs):
        # If updating, delete the old image if it is being changed.
        if self.pk:
            try:
                old_obj = HeaderImage.objects.get(pk=self.pk)
            except HeaderImage.DoesNotExist:
                old_obj = None
            if old_obj and old_obj.image and old_obj.image != self.image:
                old_obj.image.delete(save=False)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the image file when the object is deleted.
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Gallery Image {self.id} - {self.alt_text if self.alt_text else 'No Alt Text'}"
    
    def save(self, *args, **kwargs):
        # If updating, delete the old image if it is being changed.
        if self.pk:
            try:
                old_obj = GalleryImage.objects.get(pk=self.pk)
            except GalleryImage.DoesNotExist:
                old_obj = None
            if old_obj and old_obj.image and old_obj.image != self.image:
                old_obj.image.delete(save=False)
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the image file when the object is deleted.
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)