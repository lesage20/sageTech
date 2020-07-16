from django.db import models

# Create your models here.

class SocialAccount(models.Model):
    
    ICONS = {
        ('facebook', "fa-facebook"),
        ('instagram', "fa-instagram"),
        ('google-plus', "fa-google-plus-g"),
        ('linkedin', "fa-linkedin-in"),
        ('pinterest', "fa-pinterest"),
        ('flickr', "fa-flickr"),
        ('rss', "fa-rss"),
        ('dribble', "fa-dribbble"),
    }

    nom = models.CharField(max_length=255, null=True)
    lien = models.URLField(null=True)
    icon = models.CharField(choices=ICONS, max_length=20, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Social Account'
        verbose_name_plural = 'Socials Account'

    def __str__(self):
        return self.nom


class SiteInfo(models.Model):
    email = models.EmailField(max_length=255, null=True)
    logo = models.ImageField(null=True)
    

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Site Info'
        verbose_name_plural = 'Site Infos'

    def __str__(self):
        return self.email
    
class Presentation(models.Model):
    nom = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/presentation", null=True)
    video = models.URLField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254, null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
    
    def __str__(self):
        return self.email
    
class Contact(models.Model):
    mapurl = models.TextField(null=True)
    description = models.TextField(null=True)
    nom = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    website = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.nom
    