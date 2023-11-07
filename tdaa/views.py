from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse ('olá td')
def sobre (request):
    return HttpResponse ('olá td sobre')
