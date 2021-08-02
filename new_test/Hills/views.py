from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class RecipeView(TemplateView):
    template_name = 'recipe.html'


class FormView(TemplateView):
    template_name = 'form.html'


class FullView(TemplateView):
    template_name = 'full-tapenade.html'

