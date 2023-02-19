from django.contrib import admin
<<<<<<< HEAD
from .models import Gig,Skill, ProLang, Internship

# Register your models here.

admin.site.register(Gig)
=======
from .models import Skill, ProLang, Internship

# Register your models here.
>>>>>>> internship
admin.site.register(Skill)
admin.site.register(ProLang)
admin.site.register(Internship)
