from django.db import models

# Create your models here.

class Recipe(models.Model):
    picture = models.ImageField(upload_to='')
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    process = models.CharField(max_length=255)
    ingredient = models.TextField()
    