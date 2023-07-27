from typing import Any, Callable, Optional
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import New
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
   
class NewCreateView(LoginRequiredMixin, CreateView):
    model = New
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('website-index')
    
class NewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = New
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user == self.get_object().author

    
    def get_success_url(self):
        return reverse('website-index')

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})