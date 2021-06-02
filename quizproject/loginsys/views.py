from django.shortcuts import render,redirect
from .models import NewUser
from django.contrib import messages

def indexPage(request):
    return render(request,'index.html')


def userReg(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']

        NewUser(firstname=firstname,lastname=lastname,username=username,password=password).save()
        messages.success(request,"user" + firstname + "added successfully... ")

        return render(request,'registration.html')

    else:
        return render(request,'registration.html')


def loginPage(request):
    if request.method=='POST':
        try:
            UserDetails = NewUser.objects.get(username = request.POST['username'], password = request.POST['password'])
            #print("UserName : ",UserDetails)
            
            UserNameDetails = NewUser.objects.get(username = request.POST['username'])
            
            request.session['username'] = UserDetails.username
            
            request.session['firstname'] = UserNameDetails.firstname
            request.session['lastname'] = UserNameDetails.lastname
            
            #return render(request,'login.html')
            return render(request,'quiz.html')

        except NewUser.DoesNotExist as e:
            messages.success(request,"username / password is invalid...! ")

    return render(request,'login.html')

def logout(request):
    try:
       del request.sesssion['username']

    except:
       return render(request,'index.html')

    return render(request,'index.html')


def admin(request):
    response = redirect('admin')
    return render(response)

def back(request):
    return render(request,'quiz.html')