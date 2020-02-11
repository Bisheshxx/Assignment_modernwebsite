from django.db import models


# Create your models here.


class Review(models.Model):
    user = models.CharField(max_length=40)
    message = models.TextField()
    # date = models.DateTimeField()
