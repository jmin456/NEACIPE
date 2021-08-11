from django.db import models

# Create your models here.
class Neacipe(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)