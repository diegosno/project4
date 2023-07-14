from django.shortcuts import render
from .models import New
# Create your views here.


def index(request):
    context = {
        'news': New.objects.all()
    }
    return render(request, 'website/index.html', context)

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})