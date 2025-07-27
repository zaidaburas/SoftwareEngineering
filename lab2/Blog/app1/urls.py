from django.urls import path
from . import views

urlpatterns=[
    path('',views.helloApp1,name="index")
]