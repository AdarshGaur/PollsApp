# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Vorld! you're at the wrong polls index.")

