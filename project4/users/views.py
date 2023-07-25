from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import signUpForm, updateCredentials, updateProfile

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

@login_required
def profile(request):
    credentialsForm = updateCredentials()
    profileForm =  updateProfile()
    
    context = {
        'credentialsForm': credentialsForm, 
        'profileForm': profileForm
    }
    
    return render (request, 'users/profile.html', context)


# Create your views here.
