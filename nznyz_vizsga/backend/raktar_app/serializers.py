from .models import Megrendelesek
from django.db import models
from rest_framework.serializers import ModelSerializer

class MegrendelesekSerializer(ModelSerializer):
    
    
    class Meta:
        #fields = '__all__'
        fields = ['dolgozo', 'munkalap_szama', 'alapanyag','datumKezdes','datumBefejezes', 'felhasznaltMennyiseg']
        model = Megrendelesek
        depth = 1
        
        