from argparse import BooleanOptionalAction
from email.policy import default
from pyexpat import model
from statistics import mode
from typing import OrderedDict
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
    first_name  = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    
    birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    summary = models.TextField()
    bio = models.CharField(max_length=200)
    profession = models.CharField(max_length=255, blank=True, null=True)
    website= models.URLField(max_length=255, blank=True, null=True)
    freelance = models.CharField(max_length=20, choices=FREELANCE_CHOICES, default=FREELANCE_AVIALABLE)
    about = models.TextField()
    
    
    
    
    def __str__(self):
        return self.user.username
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    

            
            
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.birth.year
    
    
    
    
class Fact(models.Model):
    title = models.CharField(max_length=50)
    sub_titel = models.CharField(max_length=32)
    emoji = models.CharField(max_length=50)
    volume = models.IntegerField()
    description = models.TextField()
        
        
        
    def __str__(self):
        return self.title
        
        
    
    



class Skill(models.Model):
    title = models.CharField(max_length=100)
    volume = models.IntegerField()
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.title
    
    
    
    class Meta:
        ordering=['-title']
        
        
        
class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    grade = models.CharField(max_length=100)
    field_study = models.CharField(max_length=200)
    started_year = models.DateField(null=True, blank=True)
    ended_year = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.degree
    
    
    class Meta:
        ordering=['-ended_year']
    
class Address(models.Model):
    current_address = models.CharField(max_length=255)
    current_coutnry = models.CharField(max_length=100)
    current_city = models.CharField(max_length=155)
    home_country = models.CharField(max_length=100)
    home_city = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    
    
    
    def _str__(self):
        return self.current_address
    
    
    
class Experience(models.Model):
    EMP_CONTRACT = 'CONTRACT'
    EMP_TEM = 'TEMPRIRY'
    EMP_FULL_TIME = 'FULL_TIME'
    EMP_PART_TIME = 'PART_TIME'
    EMP_FREELANCE = "FREELANCE"
    EMP_SELF_EMPLOYED = 'SELF_EMPLOYED'
    EMP_INTRENSHIP = "INTRENSHIP"
    
    
    EMP_CHOICES = {
        ('Contract', EMP_CONTRACT),
        ('Temprary', EMP_TEM),
        ('Full Time', EMP_FULL_TIME),
        ('Part Time', EMP_PART_TIME),
        ('Freelance',EMP_FREELANCE ),
        ('Intrenship', EMP_INTRENSHIP),
        ('Self Employed', EMP_SELF_EMPLOYED)
         }
    
    
    title = models.CharField(max_length=200)
    employement_type = models.CharField(max_length=200, choices=EMP_CHOICES)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    industry = models.CharField(max_length=100)
    description = models.TextField()



    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering =['-start_date']
        
        
        
class Certificates(models.Model):
    CERTIFICATES_COMPLETED = 'Completed'
    CERTIFICATES_IN_PROGRESS = 'In Progress'
    
    CERTIFICATES_CHOICES = {
        ('Completed', CERTIFICATES_COMPLETED),
        ('In Progress', CERTIFICATES_IN_PROGRESS),
    }
    
    
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=CERTIFICATES_CHOICES, default=CERTIFICATES_COMPLETED)
    issued_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    organized = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title
    
    
    
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_text = models.CharField(max_length=200)
    
    
    
    
    def __str__(self):
        return self.title