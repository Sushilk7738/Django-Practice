from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse('<h1 style="text-align:center;">Welcome to django world</h1>')

