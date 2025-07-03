from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Students
# Create your views here.
# def greetings(request):
#     return HttpResponse("<h2>Hiee Good morning</h2>")

def index(request):
    data = Students.objects.all()
    records = {'students_data':data}
    return render(request, 'testapp/index.html', context=records)

def welcome(request):
    return HttpResponse("Welcome to python django world")