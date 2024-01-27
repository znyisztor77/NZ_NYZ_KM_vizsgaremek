from django.shortcuts import render

from .models import Megrendelesek
from .serializers import MegrendelesekSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getMegrendelesek(request):
    megrendelesek =Megrendelesek.objects.all()
    serialized =MegrendelesekSerializer(megrendelesek, many =True)

    return Response(serialized.data)