from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic.base import TemplateView

#renders index page
class indexPage(TemplateView):
    template_name = 'index.html'


#view for user registration
class userReg(View):

    def post(self,request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']

        NewUser(firstname=firstname,lastname=lastname,username=username,password=password).save()
        messages.success(request,"user  : " + firstname + " added successfully... ")

        return render(request,'registration.html')

    def get(self,request):
        return render(request,'registration.html')    


#view for login
class loginPage(View):
    
    def post(self,request):
        try:
            UserDetails = NewUser.objects.get(username = request.POST['username'], password = request.POST['password'])
                      
            UserNameDetails = NewUser.objects.get(username = request.POST['username'])
            
            request.session['username'] = UserDetails.username
            
            request.session['firstname'] = UserNameDetails.firstname
            request.session['lastname'] = UserNameDetails.lastname
                       
            return render(request,'quiz.html')

        except NewUser.DoesNotExist as e:
            messages.success(request,"username / password is invalid...! ")
            return render(request,'login.html')

    def get(self,request):
        return render(request,'login.html')


#logout view
class logout(View):
    def get(self, request, *args, **kwargs):
		#return render(request, "index.html")
        try:
           del request.sesssion['username']
        except:
           return render(request,'index.html')
    

#rendering back to quiz page
class back(TemplateView):
    template_name = 'quiz.html'