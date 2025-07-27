"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.http import HttpResponse

myAppsLinks="""
<title>Zaid Aburas</title>
<h1><a href="/app1" >Goto App1</a><h1>
<h1><a href="/app2" >Goto App2</a><h1>
<h1><a href="/app3" >Goto App3</a><h1>
"""

def mylinks(request):
    return HttpResponse(myAppsLinks)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mylinks,name="index"),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
]
