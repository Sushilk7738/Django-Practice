from django.shortcuts import render
from testapp.models import Student, Employee

# Create your views here.

def student_view(request):
    student_list = Student.objects.all()
    return render(request, 'testapp/student.html', {'student_list': student_list})


def employee_view(request):
    employee_list = Employee.objects.all()
    return render(request, 'testapp/employee.html', {'employee_list': employee_list})
