from email.policy import default
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models
from django.conf import settings



# Create your models here.
class Links(models.Model):
    title= models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    
    
    
    def __str__(self):
        return self.title
    
    
    
    
    
class Profile(models.Model):
    FREELANCE_AVIALABLE = 'true'
    FREELANCE_NOT_AVIALABLE = 'false'
    FREELANCE_CHOICES = {
        ('Available', FREELANCE_AVIALABLE),
        ('Not Available', FREELANCE_NOT_AVIALABLE),
    }
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    bio = models.CharField(max_length=200)
    profession = models.CharField(max_length=255, blank=True, null=True)
    website= models.URLField(max_length=255, blank=True, null=True)
    freelance = models.CharField(max_length=20, choices=FREELANCE_CHOICES, default=FREELANCE_AVIALABLE)
    about = models.TextField()
    
    
    
    
    def __str__(self):
        return self.user.username
    
    

            
            
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.birth.year
    
    
