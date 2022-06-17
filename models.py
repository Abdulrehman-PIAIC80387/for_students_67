from django.db import models

# Create your models here.

class Text(models.Model):
    word = models.CharField(max_length=50, blank=True,default='')
    result = models.CharField(max_length=500, blank=True,default='')
