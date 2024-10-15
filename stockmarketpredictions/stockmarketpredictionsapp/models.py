from django.db import models

# Create your models here.

class DataSetSearchBar(models.Model):
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='datasets/')
    sitename = models.CharField(max_length=150)