from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<h1>About</h1>")