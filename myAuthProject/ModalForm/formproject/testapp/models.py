from django.db import models

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    address = models.CharField(max_length=100)
    
    
class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.FloatField()