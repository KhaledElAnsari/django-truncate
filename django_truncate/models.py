from django.db import models

class Model1(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class Model2(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()
