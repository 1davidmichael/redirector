from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def detail(request, redirect_id):
    return HttpResponse("You are looking at redirect %s." % redirect_id)
