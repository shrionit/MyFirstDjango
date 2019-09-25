from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('<h1>Hello World</h1>')

def search(req, id):
    return HttpResponse(f'<h1>{id}</h1>')
        
