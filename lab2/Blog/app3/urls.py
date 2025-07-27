from django.urls import path
from . import views

urlpatterns=[
    path('',views.helloApp3,name="index")
]