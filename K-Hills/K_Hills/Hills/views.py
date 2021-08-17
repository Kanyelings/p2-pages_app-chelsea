from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class RecipePageView(TemplateView):
    template_name = 'recipe.html'


class FormPageView(TemplateView):
    template_name = 'form.html'


class TapenadePageView(TemplateView):
    template_name = 'full-tapenade.html'

