from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloApp2(request):
    return HttpResponse('<h1>Hello Application Number 2</h1>')