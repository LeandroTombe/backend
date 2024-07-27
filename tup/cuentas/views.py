from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status






class RegisterUserView(GenericAPIView):
    serializer_class=UserRegisterSerializer
    
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guarda el usuario y devuelve la instancia del usuario
            return Response({
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)