from django.urls import path
from . import views

urlpatterns=[
    path('',views.helloApp2,name="index")
]