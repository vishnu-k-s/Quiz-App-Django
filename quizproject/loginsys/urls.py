from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', admin,name="admin"),
    path('',indexPage,name="indexPage"),
    path('registration',userReg,name="RegisterPage"),
    path('login',loginPage,name="Loginpage"),
    path('logout',logout,name="LogoutPage"),


    path('',include('questionbank.urls')),


    path('back',back,name='back'),
]
