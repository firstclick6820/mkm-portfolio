from django.shortcuts import render
from . import models



# Create your views here.
def index(request):
    social_links = models.Links.objects.all()   #social Media Links
    profile = models.Profile.objects.all().first()  #Profile Info
    facts = models.Fact.objects.all()    # facts
    skills = models.Skill.objects.all() # skills
    context = {
        'links': social_links,
        'profile': profile,
        'facts': facts,
        'skills': skills,
        
    }
    return render(request,'pages/index.html', context=context)