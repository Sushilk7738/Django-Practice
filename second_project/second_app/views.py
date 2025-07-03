from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def temp_view(request):
    return render(request, 'temp.html')
