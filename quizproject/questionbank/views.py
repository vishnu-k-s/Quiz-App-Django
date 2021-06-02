from django.shortcuts import render
from .models import *
# Create your views here.


def pythonquiz(request):
    return render(request,'python.html')

def djangoquiz(request):
    return render(request,'django.html')



def pythonpage(request):
    questions = PythonQBank.objects.all()
    
    return render(request, 'python.html', { 'questions': questions})
	
	
def djangopage(request):
    questions = DjangoQBank.objects.all()
    
    return render(request, 'django.html', { 'questions': questions})
	