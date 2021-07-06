from enum import unique
from django.db import models

# Create your models here.


class Api(models.Model):
    id = models.CharField(unique, max_length=200, primary_key=True)
    quote = models.CharField(max_length=400)
    speaker = models.CharField(max_length=40)
    pic = models.ImageField(upload_to="images/", null=True, blank=True)
