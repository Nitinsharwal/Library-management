from django.contrib import admin
from django.urls import path,include
from ntin import views
urlpatterns = [
    path('index',views.index,name='nitin'),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
]
