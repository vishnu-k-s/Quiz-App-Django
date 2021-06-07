from django.shortcuts import render
from .models import *
from django.views.generic.base import TemplateView

#rendering python page
class pythonpage(TemplateView):
    template_name = 'python.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = PythonQBank.objects.all()
        return context	


#rendering django page
class djangopage(TemplateView):
    template_name = 'django.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = DjangoQBank.objects.all()
        return context	


#rendering quantitative page
class quantitativepage(TemplateView):
    template_name = 'quantitative.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = QuantitativeQBank.objects.all()
        return context	


#rendering java page
class javapage(TemplateView):
    template_name = 'java.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = JavaQBank.objects.all()
        return context	