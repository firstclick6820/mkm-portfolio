from django.contrib import admin
from .models import Links


# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Links,LinksAdmin)    
    
    
