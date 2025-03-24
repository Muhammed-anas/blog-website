from django.urls import path

from .views import main_page,home_page, contact_page, about_page, create_post, post_listing

urlpatterns = [
    path('', main_page, name='main'),
    path('home/', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('new-post/', create_post, name='new_post'),
    path('post-listing/<str:id>/details/', post_listing, name='post_list'),
]



