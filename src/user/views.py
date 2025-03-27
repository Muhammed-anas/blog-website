from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def register_view(request):
    register_form = UserCreationForm()
    return render (request, 'views/registration.html',
                   {'register_form':register_form})


def login_view(request):
    login_form = AuthenticationForm()
    return render(request, 'views/login.html',
                  {'login_form':login_form})

