from .models import Megrendelesek, CustomUser
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name']

class MegrendelesekSerializer(serializers.ModelSerializer):
    dolgozo = CustomUserSerializer( read_only=True)
    class Meta:

        model = Megrendelesek
        fields = ['id','dolgozo', 'munkalap_szama', 'alapanyag','datumKezdes','datumBefejezes', 'felhasznaltMennyiseg']
        depth = 1
        





       