from site import addusersitepackages
from django.shortcuts import render
from . import models



# Create your views here.
def index(request):
    social_links = models.Links.objects.all()   #social Media Links
    profile = models.Profile.objects.all().first()  #Profile Info
    facts = models.Fact.objects.all()    # facts
    skills = models.Skill.objects.all() # skills
    education = models.Education.objects.all()
    address = models.Address.objects.all()
    experiences = models.Experience.objects.all()
    
    context = {
        'links': social_links,
        'profile': profile,
        'facts': facts,
        'skills': skills,
        'educations': education,
        'addresses': address,
        'experiences':experiences
        
    }
    return render(request,'pages/index.html', context=context)