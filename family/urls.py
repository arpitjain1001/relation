from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path('index/',views.index),
 path('about/',views.about),
 path('contact/',views.contact),

 

]