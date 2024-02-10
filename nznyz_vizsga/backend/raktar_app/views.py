from django.shortcuts import render
from django.http import HttpResponse
from .models import Megrendelesek, Alapanyag
from .serializers import MegrendelesekSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView
from django.shortcuts import render,redirect, get_object_or_404
from .forms import LoginForm,BevitelForm, KiadasForm, MegrendelesForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .admin import CustomUser

@api_view(['GET'])
def getMegrendelesek(request):
    megrendelesek =Megrendelesek.objects.all().prefetch_related('alapanyag')
    serialized =MegrendelesekSerializer(megrendelesek, many =True)

    return Response(serialized.data)


def home(request):

    return render(request, 'home.html')

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

def bevitel_kiadas( request):
     bevform = BevitelForm()
     kiform = KiadasForm()
     alapanyagok_lista = Alapanyag.objects.all()               

     if request.method == 'POST':  
        bevform = BevitelForm(request.POST)
        if bevform.is_valid():
             if Alapanyag.objects.filter(anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                                         vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                                         meret_valaszt = bevform.cleaned_data['meret_valaszt'],).exists():
                messages.error(request, f'"{bevform.cleaned_data["anyagtipusa"]}, {bevform.cleaned_data["vastagsag_valaszt"]}, {bevform.cleaned_data["meret_valaszt"]}" ilyen anyag ezekkel a paraméterekkel, már van a raktárban!')
             else:
                ujanyag = Alapanyag.objects.create(
                    anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                    vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                    meret_valaszt = bevform.cleaned_data['meret_valaszt'],
                    darabszam = bevform.cleaned_data['darabszam'],
                    polc_szama = bevform.cleaned_data['polc_szama'],
                    rogzit_datum = bevform.cleaned_data['rogzit_datum'],)
                ujanyag.save()
                   
        kiform = KiadasForm(request.POST)

        if kiform.is_valid():
            kiform.save()
           
     return render(request, 'raktar.html', { 'object_list':alapanyagok_lista,
                                            'bevform': bevform,
                                            'kiform': kiform })

def megrendeles(request):
    dolgform = MegrendelesForm()
    megrendelesek_lista = Megrendelesek.objects.all() 
    if request.method == 'POST':
        dolgform = MegrendelesForm(request.POST)
        if dolgform.is_valid():
            dolgform.save()  

    return render(request, 'dolgozo.html', { 'object_list':megrendelesek_lista,
                                            'dolgform': dolgform})

def logout_page(request):
    logout(request)
    return redirect('login')

class HomeView(ListView):
    model = Megrendelesek
    template_name = 'home.html'
class DolgozoView(ListView):
    model = Megrendelesek
    template_name = 'dolgozo.html'
'''class RaktarView(ListView):
    model = Alapanyag 
    template_name = 'raktar.html' '''










