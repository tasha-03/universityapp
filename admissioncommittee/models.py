from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=5)
    cathedra = models.CharField(choices=((
        "1", "Gryffindor"), ("2", "Hufflepuff"), ("3", "Ravenclaw"), ("4", "Slytherin")), max_length=1)
