from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, "home.html")

def introduction(request):
    return render(request , "introduction.html")

def programers(request):
    return render(request, "programers.html")
