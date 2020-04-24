# from django.db import models
from djongo import models


# Create your models here.
class Bot(models.Model):
    name = models.CharField(max_length=250)
    language = models.CharField(max_length=250)


class Scenes(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=50)


class Intent(models.Model):
    name = models.CharField(max_length=250)
    message = models.CharField(max_length=500)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default="in_progress")
    intent_image = models.ImageField(upload_to='i/%Y/%m/%d/%H/%M/', max_length=512, null=True, blank=True)
