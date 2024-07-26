from django.shortcuts import render

from rest_framework import generics
from .models import Materia, Cuota, Alumno, Cursado, CompromisoPago, Pago, Inhabilitation, Coordinador, Mensajes
from .serializers import MateriaSerializer, CuotaSerializer, AlumnoSerializer, CursadoSerializer, CompromisoPagoSerializer, PagoSerializer, InhabilitationSerializer, CoordinadorSerializer, MensajesSerializer



class MateriaListCreateView(generics.ListCreateAPIView):
    
    serializer_class = MateriaSerializer
    
    def get_queryset(self):
        queryset = Materia.objects.all()
        materia = self.request.query_params.get('materia')
        if materia is not None:
            queryset = queryset.filter(materia=materia)
        return queryset
    