from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('recipe/', RecipePageView.as_view(), name='recipe'),
    path('form/', FormPageView.as_view(), name='form'),
    path('full/', TapenadePageView.as_view(), name='tapenade'),
]