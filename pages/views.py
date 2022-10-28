from django.shortcuts import render
from . import models



# Create your views here.
def index(request):
    social_links = models.Links.objects.all()   #social Media Links
    
    
    context = {
        'links': social_links
        
    }
    return render(request,'pages/index.html', context=context)