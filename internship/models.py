from django.db import models
from company.models import Company

class Internship(models.Model):
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=5000, default="")
    category = models.CharField(max_length=5000, default="")
    open_date = models.DateField(null=True)
    closing_date = models.DateField(null=True)

    def __str__(self):
        return self.title
    


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    Internship =  models.ForeignKey(Internship, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

class ProLang(models.Model):
    ProLang = models.CharField(max_length=100)
    Internship =  models.ForeignKey(Internship, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProLang


class Gig(models.Model):
    Internship = models.OneToOneField(Internship, on_delete=models.CASCADE)
    open_date = models.DateField()
    closing_date = models.DateField()


    