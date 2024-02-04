from django.shortcuts import render
from django.http import HttpResponse
from .models import Megrendelesek, Alapanyag
from .serializers import MegrendelesekSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView
from django.shortcuts import render,redirect
from .forms import LoginForm,BevitelForm, KiadasForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

@api_view(['GET'])
def getMegrendelesek(request):
    megrendelesek =Megrendelesek.objects.all().prefetch_related('alapanyag')
    serialized =MegrendelesekSerializer(megrendelesek, many =True)

    return Response(serialized.data)

class RaktarView(ListView):
    model = Alapanyag 
    template_name = 'raktar.html' 

class DolgozoView(ListView):
    model = Megrendelesek
    template_name = 'dolgozo.html' 

class HomeView(ListView):
    model = Megrendelesek
    template_name = 'home.html'




def home(request):

    return render(request, 'home.html')

def raktar(request):
    
    return render(request, 'raktar.html')

def dolgozo(request):
    
    return render(request, 'dolgozo.html')


def bejelentkezes(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user and user.raktaros==True:
                login(request, user)
                messages.success(request, f' Hello {username.title()}, ujra itt!')
                
                return redirect('raktar')
            elif user and user.lezervago == True:
                login(request, user)
                messages.success(request, f' Hello {username.title()}, ujra itt!')
                return redirect('dolgozo')
        
        messages.error(request, f'Helytelen felhasználónév vagy jelszó') 
        return render(request, 'login.html', {'form':form})   


def logout_page(request):
    logout(request)
    return redirect('login')

def bevitel(request):
    #request.method == 'POST'
    #bevform = BevitelForm(request.POST)
    bevform = BevitelForm()
    return render(request, 'raktar.html', {'bevform': bevform})



'''def kiadas(request):
    form = KiadasForm()
    return render(request, 'raktar.html', {'form': form})'''