from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def one(request):
    return render(request,'showone.html')

def edit(request):
    return render(request,'edit.html')

def delete(request):
    return render(request,'delete.html')

def var(request):
    data=[
        {"name":"Ali","age":25,},
        {"name":"Ahmed","age":17,},
        {"name":"Nader","age":20,},
        {"name":"Saleh","age":50,},
    ]
    return render(request,'var.html',{"data":data})

def filters(request):
    context = {
        "name": "ahmed ali",
        "empty_value": "",
        "none_value": None,
        "items": ["item1", "item2", "item3"],
        "number": 10,
        "big_number": 12345678,
        "html_code": "<b>Hello</b>",
        "pi": 3.14159,
        "text": "any text",
        "today": datetime.now(),
    }
    return render(request, "filters.html", context)
