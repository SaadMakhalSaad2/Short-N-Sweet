from re import template
from django.db import models

# Create your models here.

class URLData(models.Model):
    URLID = models.CharField(max_length = 1000)
    ShortURL = models.CharField(max_length = 1000)

    def __str__(self):
        template = '{0.URLID}, {0.ShortURL}'
        return template.format(self)

