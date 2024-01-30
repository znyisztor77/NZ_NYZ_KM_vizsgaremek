from django.shortcuts import render
from django.http import HttpResponse
from .models import Megrendelesek
from .serializers import MegrendelesekSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView

@api_view(['GET'])
def getMegrendelesek(request):
    megrendelesek =Megrendelesek.objects.all()
    serialized =MegrendelesekSerializer(megrendelesek, many =True)

    return Response(serialized.data)

class HomeView(ListView):
    model = Megrendelesek
    template_name = 'home.html'

def home(request):
    megrendelesek = Megrendelesek.objects.all().prefetch_related('alapanyag')
    context = {
        'Megrendelések': megrendelesek
    }
    return render(request, 'home.html', context)