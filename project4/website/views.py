from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

news = [
    {
        'title': 'Summer',
        'author': 'Diego',
        'content': 'Summer content',
        'date_created': 'July 12, 2022'
        }
    ,
    {'title': 'Brunch',
        'author': 'Dany',
        'content': 'Brunch content',
        'date_created': 'July 13, 2022'
        
    }
        
    
]
def index(request):
    context ={
        'news': news
    }
    return render(request, 'website/index.html', context)

def contact(request):
    return render(request, 'website/contact.html')