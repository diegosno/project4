from typing import Any, Callable, Optional
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import New
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import signUpForm, updateCredentials, updateProfile

# Create your views here.


def index(request):
    context = {
        'news': New.objects.all(),

    }
  
    return render(request, 'website/index.html', context)

class NewListView(ListView):
    model = New
    template_name = 'website/index.html'
    context_object_name = 'news'
    ordering = ['-date_created'] 
    paginate_by = 3
    
class UserNewListView(ListView):
    model = New
    template_name = 'website/index.html'
    context_object_name = 'news'
    ordering = ['-date_created'] 
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return New.objects.filter(author=user).order_by('-date_created')
        
    
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
    
class NewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = New
    success_url = "/"
    
    def test_func(self):
        return self.request.user == self.get_object().author
          


def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact'})


def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
       
            messages.success(request, f'Welcome {username}! Login to continue. ')
            return redirect('login')

    else:
        form = signUpForm()
    return render(request, 'website/signup.html', {'form': form} )

@login_required
def profile(request):
    if request.method == 'POST':
        credentialsForm = updateCredentials(request.POST, instance=request.user)
        profileForm =  updateProfile(request.POST, request.FILES, instance=request.user.profile)
        if credentialsForm.is_valid() and profileForm.is_valid():
            credentialsForm.save()
            profileForm.save()

            messages.success(request, f'Data updated succesfully.')
            return redirect('profile')
            
    else:
        credentialsForm = updateCredentials(instance=request.user)
        profileForm =  updateProfile(instance=request.user.profile)
    
    context = {
        'credentialsForm': credentialsForm, 
        'profileForm': profileForm
    }
    
    return render (request, 'website/profile.html', context)