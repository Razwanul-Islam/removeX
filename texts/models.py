from django.db import models

# Create your models here.

class SectionTitle(models.Model):
    SECTIONS = [
        ('about', 'About Section Title'),
        ('services', 'Services Section Title'),
        ('process', 'Process Section Title'),
        ('gallery', 'Gallery Section Title'),
        ('contact', 'Contact Section Title')
    ]
    section = models.CharField(max_length=20, choices=SECTIONS, unique=True)
    title = models.CharField(max_length=100)

class HeaderText(models.Model):
    TYPE = [
        ('hero-title', 'Hero Title'),
        ('hero-subtitle', 'Hero Subtitle'),
        ('hero-button-text', 'Hero Button Text')
    ]
    type = models.CharField(max_length=20, choices=TYPE, unique=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.type}"
    
class AboutCard(models.Model):
    curcle_icon = models.CharField(max_length=2,help_text="Special characters: ★, ✔, ✘, ➔, ➽, ❖")
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return f"{self.title}"
    
class ServiceCard(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    list_of_services = models.TextField(help_text="Use new line to separate services")


class ProcessCard(models.Model):
    step_number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
    

class ContactInfo(models.Model):
    TYPE = [
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('address', 'Address'),
        ('hours', 'Hours')
    ]
    type = models.CharField(max_length=20, choices=TYPE, unique=True)
    content = models.TextField()


class FooterText(models.Model):
    TYPE = [
        ('below-logo', 'Text Below Logo'),
        ('copyright', 'Copyright Text')
    ]
    type = models.CharField(max_length=20, choices=TYPE, unique=True)
    content = models.TextField()