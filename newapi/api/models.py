from statistics import mode
from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    employeeid = models.IntegerField()
    phone = models.CharField(max_length=15)
    address= models.CharField(max_length=100)

    class Meta:
        ordering = ['-id',]
        

    def __str__(self):
        return self.firstname
