from django.db import models

#Users
class Users(models.Model):
    name = models.CharField(max_length=25)
    username= models.CharField(max_length=15, unique=True)
    password= models.CharField(max_length=150)
    university = models.CharField(max_length=50)
    degree = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
