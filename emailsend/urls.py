from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path('others/',views.send_email)
 

]