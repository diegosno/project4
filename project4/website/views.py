from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import New
from django.urls import reverse
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
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('website-index')

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})