import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name
"""
class AccountData(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    password = models.CharField(max_length=200)
    #other account stuff
    def __str__(self):
        return self.password
"""

