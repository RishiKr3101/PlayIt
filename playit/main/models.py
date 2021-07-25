from django.db import models

# Create your models here.

#Name of all university
class University(models.Model):
    university = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.university
    

#Degrees available in University
class Degrees(models.Model):
    university= models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.degree


#Courses available in Degree
class Courses(models.Model):
    degree= models.ForeignKey(Degrees, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.course




