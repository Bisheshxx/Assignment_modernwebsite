from django.db import models

# Create your models here.

class register(models.Model):
    user_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    password2 = models.CharField(max_length=40)