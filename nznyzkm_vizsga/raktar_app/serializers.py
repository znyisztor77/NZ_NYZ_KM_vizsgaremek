from .models import Megrendelesek, CustomUser
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']

class MegrendelesekSerializer(serializers.ModelSerializer):
    dolgozo = CustomUserSerializer( read_only=True)
    class Meta:
        #fields = '__all__'
        model = Megrendelesek
        fields = ['dolgozo', 'munkalap_szama', 'alapanyag','datumKezdes','datumBefejezes', 'felhasznaltMennyiseg']
        
        depth = 1
        





       