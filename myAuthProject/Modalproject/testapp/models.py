from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=128)
    esal = models.FloatField()
    age = models.IntegerField()
    
    
class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    stream = models.CharField(max_length=50)