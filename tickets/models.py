from django.db import models

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie_name = models.CharField(max_length=100)
    movie_date = models.DateField(max_length=10)
    category = models.CharField(max_length=10)

class Guest(models.Model):
    guest_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete= models.CASCADE)
    
    
# Create your models here.
