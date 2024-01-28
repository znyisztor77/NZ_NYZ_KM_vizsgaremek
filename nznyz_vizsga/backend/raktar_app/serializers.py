from .models import Megrendelesek
from rest_framework.serializers import ModelSerializer

class MegrendelesekSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Megrendelesek
        depth = 2
        
        