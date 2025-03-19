from django.urls import path

from .views import main_page,home_page, contact_page, about_page

urlpatterns = [
    path('', main_page, name='main'),
    path('home/', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about')
    
]



