from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField

# Create your models here.
class Location(models.Model):
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = USStateField(max_length=20, default='NY')
    
    def __str__(self):
        return f'{self.id} Location'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    bio = models.CharField(max_length=150, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, 
                                    null=True)
    
    
    def __str__(self):
        return f'{self.user.username} details'