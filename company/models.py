from django.db import models

class company(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=5000, default="")
    email  = models.EmailField()
    
   