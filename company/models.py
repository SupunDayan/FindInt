from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=5000, default="")
    email  = models.EmailField()

    def __str__(self):
        return self.name + ' - ' + self.description

    
   