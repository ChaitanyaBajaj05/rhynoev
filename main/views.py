# main/views.py
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.conf import settings


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

def contact_us(request):
    return render(request, 'main/contact.html')

def rentals(request):
    return render(request, 'main/rentals.html')









