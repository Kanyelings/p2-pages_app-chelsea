from django.urls import path
from .views import HomeView, RecipeView, FormView, FullView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/', RecipeView.as_view(), name='recipe'),
    path('form/', FormView.as_view(), name='form'),
    path('recipe/full/', FullView.as_view(), name='full'),
]