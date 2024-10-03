from django.db import models

# Create your models here

class Employee(models.Model):

    name=models.CharField(max_length=30)

    designation=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    contact=models.CharField(max_length=200)

    salary=models.IntegerField()

    address=models.CharField(max_length=200)