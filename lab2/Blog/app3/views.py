from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloApp3(request):
    return HttpResponse('<h1>Hello Application Number 3</h1>')