from rest_framework import viewsets
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer

# API CRUD
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Frontend UI
def employee_list_ui(request):
    employees = Employee.objects.all()
    return render(request, "employees.html", {"employees": employees})
