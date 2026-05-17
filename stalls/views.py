from django.shortcuts import render

def index(request):
    return render(request, 'stalls/index.html')