from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} <{self.email}> at {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"   

# Contact us reciver mail list
class ContactUsReceiver(models.Model):   
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Us Receiver"
        verbose_name_plural = "Contact Us Receivers"
