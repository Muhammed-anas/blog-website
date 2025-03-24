from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

def main_page(request):
    return render (request, 'views/main.html')

def home_page(request):
    all_posts = Post.objects.all()
    return render (request, 'views/home.html',{
        'all_posts':all_posts })

def contact_page(request):
    return render (request, 'views/contact.html')

def about_page(request):
    return render (request, 'views/about.html')

def create_post(request):
    return render (request, 'components/create-post.html')

def post_listing(request,id):
    all_posts = Post.objects.filter(id=id)
    return render (request,'components/post.html',
                   {'all_posts':all_posts})
