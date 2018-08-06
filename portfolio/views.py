from django.shortcuts import render
from .models import Project
from django.views.generic import TemplateView

# Create your views here.

class Portfolio(TemplateView):
    template_name = "portfolio/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context