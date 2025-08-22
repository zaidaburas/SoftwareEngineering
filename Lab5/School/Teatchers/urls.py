from django.urls import path
from . import views
from . import views2

# model form

""" urlpatterns = [
    path('', views.getAll, name="getAll"),
    path('create/', views.create, name="create"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
] """


# python form

urlpatterns = [
    path('', views.getAll, name="getAll"),
    path('create/', views2.create, name="create"),
    path('update/<int:id>/', views2.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
