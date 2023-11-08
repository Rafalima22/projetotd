from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render (request, 'tdaa/home.html')
def sobre (request):
    return render (request, 'tdaa/sobre.html')
def contato (request):
    return render (request, 'tdaa/contato.html')
def blog (request):
    return render (request, 'tdaa/blog.html')

