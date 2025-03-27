from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    return render (request, 'views/register.html')

@login_required
def login_view(request):
    return render(request, 'views/login.html')

