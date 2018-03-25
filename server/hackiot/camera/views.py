from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You should see a live video feed here?")

# Create your views here.
