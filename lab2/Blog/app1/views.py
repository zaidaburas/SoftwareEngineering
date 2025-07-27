from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloApp1(request):
    return HttpResponse('<h1>Hello Application Number 1</h1>')