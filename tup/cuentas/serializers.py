from rest_framework import serializers
from .models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model=User
        fields=['email','nombre', 'apellido', 'password', 'password2']
        
        
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_date):
        return super().create(validated_date)