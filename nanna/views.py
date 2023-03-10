from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nana(request):
    return HttpResponse('<h1>my father is my heart</h1>')