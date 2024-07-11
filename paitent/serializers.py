from .models import Paitent
from rest_framework import viewsets
from rest_framework import serializers
from django.contrib.auth.models import User

from django.db import models

class PaitentModelSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta: 
        model=Paitent
        fields="__all__"


class UserentRegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required = True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']
    
    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']
        email=self.validated_data['email']
        confirm_password=self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'error':"Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"This email already exist"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':"This username already exist"})
        
        account=User(username=username,email=email)
        account.set_password(password)
        account.is_active=False
        account.save()
        print(account)
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

        