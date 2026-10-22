from django.shortcuts import render
from django.http import HttpResponse

def http_test(respond):
    return HttpResponse("hello word")