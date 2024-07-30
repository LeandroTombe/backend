from django.urls import path

from .views import MateriasView

urlpatterns = [
    path('materia/', MateriasView.as_view()),
    
]
