from http.client import HTTPResponse
from pipes import Template
from re import template
from urllib import request
from django.shortcuts import render
from django.template import Template,Context
# Create your views here.

def index(request):
    return render(request,"index.html")
    
def contacto(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
