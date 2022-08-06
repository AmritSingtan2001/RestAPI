from pyexpat import model
from statistics import mode
from attr import field
from rest_framework import serializers
from . models import Book,Auther
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = '__all__'


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = '__all__'
        