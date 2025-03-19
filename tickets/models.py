from django.db import models

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie_name = models.CharField(max_length=100)
    movie_date = models.DateField(max_length=10)
    category = models.CharField(max_length=10)

class guest():
    guest_name = models.CharField(max_length=100)
    
# Create your models here.
