from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee, Student
# Create your views here.

def emp_list_val(request):
    emplist = Employee.objects.all()
    return render(request, "testapp/index.html", context={"emplist":emplist})

def student_list_val(request):
    studentlist = Student.objects.all()
    return render(request, 'testapp/student.html', context= {"studentlist": studentlist})

