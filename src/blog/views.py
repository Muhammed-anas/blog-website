from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import postForms
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
    if request.method == 'POST':
        listing_form = postForms(request.POST, request.FILES)
    elif request.method == 'GET':
        listing_form = postForms()
    return render (request, 'components/create-post.html',
                   {'listing_form':listing_form})

def post_listing(request,id):
    all_posts = Post.objects.filter(id=id)
    return render (request,'components/post.html',
                   {'all_posts':all_posts})
