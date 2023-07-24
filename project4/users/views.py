from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import signUpForm

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
    return render(request, 'users/signup.html', {'form': form} )



# Create your views here.
