from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, aauthenticate
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'GET':
        register_form = UserCreationForm()
        
    elif request.method == 'POST':
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f'User {user.username} registered successfully')
            return redirect ('home')
        else:
            messages.error(request,'There is an error occured')
    return render (request, 'views/registration.html',
                    {'register_form':register_form})



def login_view(request):
    login_form = AuthenticationForm()
    return render(request, 'views/login.html',
                  {'login_form':login_form})

 