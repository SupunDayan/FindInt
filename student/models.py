from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)

