from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def news_view(request):
    return render(request, 'home.html')


def cric_view(request):
    msg1 = "Mahendra Singh Dhoni is honoured with ICC:Hall Of Fame"
    msg2 = "Virat Kohli retired from test format of indian cricket"
    return render(request, 'cri.html',{'msg1':msg1, 'msg2':msg2})

def bolly_view(request):
    return render(request, 'bollywood.html')

def polly_view(request):
    return render(request, 'politics.html')

def glam_view(request):
    return render(request, 'glam.html')