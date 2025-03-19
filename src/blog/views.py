from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def main_page(request):
    return render (request, 'views/main.html')

def home_page(request):
    return render (request, 'views/home.html')

def contact_page(request):
    return render (request, 'views/contact.html')

def about_page(request):
    return render (request, 'views/about.html')
