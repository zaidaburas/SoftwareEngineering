from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('getone/',views.one,name='one'),
    path('edit/',views.edit,name='edit'),
    path('delete/',views.delete,name='delete'),
    path('var/',views.var,name='var'),
    path('filters/',views.filters,name='filters'),
]