from django.db import models

class StudentDet(models.Model):
    stu_name=models.CharField(max_length=100, default="")
    degree=models.CharField(max_length=100, default="")
    university=models.CharField(max_length=100, default="")
    pro_email=models.CharField(max_length=100, default="")
    linkedin=models.CharField(max_length=100, default="")
    github=models.CharField(max_length=100, default="")


class ProLang(models.Model):
    student_det = models.ForeignKey(StudentDet, models.DO_NOTHING)
    language = models.CharField(max_length=20)


class Skill(models.Model):
    student_det = models.ForeignKey(StudentDet, models.DO_NOTHING)
    skill = models.CharField(max_length=50)
