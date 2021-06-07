from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
   
    path('pythonquizpage',pythonpage.as_view(),name='pythonquizpage'),
    path('djangoquizpage',djangopage.as_view(),name='djangoquizpage'),
    path('quantitativequizpage',quantitativepage.as_view(),name='quantitativequizpage'),
    path('javaquizpage',javapage.as_view(),name='javaquizpage'),

]