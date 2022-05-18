from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1024)
    date = models.DateField()
    text = models.CharField(max_length=1024)
    rating = models.FloatField()
