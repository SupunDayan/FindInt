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



# class Person(models.Model):
#     id = models.BigIntegerField(primary_key=True, db_column='person_id')
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'person'


# class PhoneNumbers(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     person = models.ForeignKey(Person, models.DO_NOTHING)
#     phone_number = models.CharField(max_length=15)
#     area_code = models.CharField(max_length=15)

#     class Meta:
#         db_table = 'phonenumbers'
#         unique_together = (('person', 'phone_number', 'area_code'),)