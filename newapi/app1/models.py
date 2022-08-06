from turtle import ondrag
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)

    class Meta:
        ordering= ['-id',]

    def __str__(self):
        return self.book_name

class Auther(models.Model):
    book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name= 'book')
    authername = models.CharField(max_length=100)
    address = models.CharField(max_length=50)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.authername
