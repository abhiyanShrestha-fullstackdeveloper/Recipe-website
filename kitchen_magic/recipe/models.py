from django.db import models

# Create your models here.

class Recipe(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    description = models.TextField()
    process = models.ForeignKey('Process',on_delete=models.CASCADE)
    ingredient = models.TextField()

class Category(models.Model):
    category = models.CharField(max_length=255)
    

class Process(models.Model):
    process = models.CharField(max_length=255)
    