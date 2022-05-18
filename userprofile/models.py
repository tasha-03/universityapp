from django.db import models
from admissioncommittee.models import Course


class User(models.Model):
    full_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self")
    password = models.CharField(max_length=60)


class Anketa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    birthday = models.DateField()
