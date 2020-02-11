from django.db import models

# Create your models here.


class Reservation(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Bike = models.CharField(max_length=40)
    datefrom = models.DateField()
    dateto = models.DateField()
