from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signUp(request):
    form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form} )
    

# Create your views here.
