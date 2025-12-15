from django.db import models

class Income(models.Model):
    value = models.FloatField()
    frequency = models.CharField()
    aggression = models.CharField()

class Expense(models.Model):
    name = models.CharField()
    date = models.DateField(null=True, blank=True)
    value = models.FloatField()
    method = models.CharField()
    frequency = models.CharField()
    category = models.CharField()
    description = models.CharField(max_length=200)
