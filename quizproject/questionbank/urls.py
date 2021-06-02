from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    #below is unuse
    path('pythonquiz',pythonquiz,name='PythonPage'),
    #above
    path('djangoquiz',djangoquiz,name='DjangoPage'),


    
    path('pythonquizpage',pythonpage,name='pythonquizpage'),
    path('djangoquizpage',djangopage,name='djangoquizpage'),


    #path('back',back,name='goback'),

]