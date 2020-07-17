from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=True)
    username = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    image = models.ImageField(null=True)
    phone = PhoneField(null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
    
