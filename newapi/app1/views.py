from multiprocessing import managers
from django.shortcuts import render
from . models import Book, Auther
from .serializers import BookSerializer, AutherSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view






@api_view(['GET'])
def listBook(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many= True)
    return Response(serializer.data)

    

@api_view(['GET'])
def listAuther(request):
    auther = Auther.objects.all()
    serializers = AutherSerializer(auther, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def bookdetail(request, pk):
    details = Book.objects.get(id=pk)
    serializers = BookSerializer(details, many = False)
    return Response(serializers.data)


@api_view(['GET'])
def autherdetail(request, pk):
    details = Auther.objects.get(id=pk)
    serializers = AutherSerializer(details, many= False)
    return Response(serializers.data)

@api_view(['POST'])
def bookinsert(request):
    serializers = BookSerializer( data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def autherinsert(request):
    serializers = AutherSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['POST'])
def bookupdate(request, pk):
    id = request.POST.get(pk)
    serializers= BookSerializer(instance= id, data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def autherupdate(request, pk):
    id = request.POST.get(pk)
    serializers= AutherSerializer(instance= id, data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
@api_view(['DELETE'])
def bookdelete(request, pk):
    serializers = Book.objects.get(id= pk)
    serializers.delete()
    return Response("Item delete successfully!!")


@api_view(['DELETE'])
def autherdelete(request, pk):
    serializers = Auther.objects.get(id= pk)
    serializers.delete()
    return Response("Item delete successfully!!")