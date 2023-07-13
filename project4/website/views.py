from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')