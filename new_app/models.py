import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField()
