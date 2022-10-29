from django.contrib import admin
from .models import Links, Profile, Fact, Skill, Education, Address, Experience


# Register your models here.
class LinksAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Links,LinksAdmin)    
    
    
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bio']
  
admin.site.register(Profile, ProfileAdmin)
    
    
    
class FactAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Fact, FactAdmin)



class SkillAdmin(admin.ModelAdmin):
    list_display= ['title']
    
admin.site.register(Skill, SkillAdmin)



class EducationAdmin(admin.ModelAdmin):
    list_display= ['degree', 'school']
    
    
    
admin.site.register(Education, EducationAdmin)





class AddressAdmin(admin.ModelAdmin):
    list_display = ['current_address', 'home_address']
    
    
admin.site.register(Address, AddressAdmin)



class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name']
    
    
admin.site.register(Experience, ExperienceAdmin)