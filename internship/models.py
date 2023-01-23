from django.db import models
from company.models import company

class Internship(models.Model):
    company =  models.ForeignKey(company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=5000, default="")
    category = models.CharField(max_length=5000, default="")
    open_date = models.DateField(null=True)
    closing_date = models.DateField(null=True)


class Skill(models.Model):
    skill = models.CharField(max_length=100)
    Internship =  models.ForeignKey(Internship, on_delete=models.CASCADE)


class ProLang(models.Model):
    ProLang = models.CharField(max_length=100)
    Internship =  models.ForeignKey(Internship, on_delete=models.CASCADE)




    