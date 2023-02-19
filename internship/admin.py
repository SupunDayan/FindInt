from django.contrib import admin
from .models import Gig,Skill, ProLang, Internship

# Register your models here.

admin.site.register(Gig)
admin.site.register(Skill)
admin.site.register(ProLang)
admin.site.register(Internship)
