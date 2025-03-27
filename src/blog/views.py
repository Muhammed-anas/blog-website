from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

@login_required
def create_post(request):
    if request.method == 'POST':
        try:
            listing_form = postForms(request.POST, request.FILES)
            if listing_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.author = request.user.profile
                listing.save()
                messages.info(request,f'new post was created')
                return redirect('home')
            else:
                raise Exception
        except Exception as e:
            print(e)  
    elif request.method == 'GET':
        listing_form = postForms()
    return render (request, 'components/create-post.html',
                   {'listing_form':listing_form})

def post_listing(request,id):
    all_posts = Post.objects.filter(id=id)
    return render (request,'components/post.html',
                   {'all_posts':all_posts})
