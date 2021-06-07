from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.generic.base import RedirectView


urlpatterns = [
    #including path of questionbank 
    path('',include('questionbank.urls')),
    path('',indexPage.as_view(),name="indexPage"),
    #redirecting to admin using RedirectView
    path('admin/', RedirectView.as_view(),name="admin"),    
    path('registration',userReg.as_view(),name="RegisterPage"),
    path('login',loginPage.as_view(),name="Loginpage"), 
    path('logout',logout.as_view(),name="LogoutPage"),
    path('back',back.as_view(),name='back'),
]
