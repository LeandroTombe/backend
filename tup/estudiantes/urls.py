from django.urls import path

from .views import MateriaListCreateView

urlpatterns = [
    path('materia/', MateriaListCreateView.as_view()),
    
]
