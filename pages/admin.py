from django.contrib import admin
from .models import Links, Profile


# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Links,LinksAdmin)    
    
    
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bio']
  
admin.site.register(Profile, ProfileAdmin)
    
