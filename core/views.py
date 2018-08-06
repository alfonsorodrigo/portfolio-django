from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "core/home.html"

class About(TemplateView):
    template_name = "core/about.html"

class Contact(TemplateView):
    template_name = "core/contact.html"