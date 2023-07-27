from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import New
# Create your views here.


def index(request):
    context = {
        'news': New.objects.all()
    }
    return render(request, 'website/index.html', context)

class NewListView(ListView):
    model = New
    template_name = 'website/index.html'
    context_object_name = 'news'
    ordering = ['-date_created'] 
    
class NewDetailView(DetailView):
    model = New
   
class NewCreateView(CreateView):
    model = New
    fields = ['title', 'content']

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})