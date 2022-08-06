from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer


class  UserViewset(viewsets.ModelViewSet):
    pass
