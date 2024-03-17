from django.shortcuts import render
from django.http import HttpResponse
from .models import Megrendelesek, Alapanyag
from .serializers import MegrendelesekSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView
from django.shortcuts import render,redirect
from .forms import LoginForm,BevitelForm, KiadasForm, MegrendelesForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import F
from django.utils import timezone
from django.conf import settings




#from qr_code import *
#import qr_code


@api_view(['GET'])
def getMegrendelesek(request):
    megrendelesek =Megrendelesek.objects.all() 
    serialized =MegrendelesekSerializer(megrendelesek, many =True)

    return Response(serialized.data)


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        port = request.META.get('SERVER_PORT')
        qr = (ip+":"+port)
    return render(request, 'home.html',{'ip': ip, 'port': port, 'qr':qr})



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

            if user and user.raktaros == True:
                       
               login(request, user)
               messages.success(request, f' Hello {username.title()}, ujra itt!')                
               return redirect('raktar')
            
            elif user and user.lezervago == True:
                login(request, user)
                messages.success(request, f' Hello {username.title()}, ujra itt!')
                return redirect('megrendeles')
        
        messages.error(request, f'Helytelen felhasználónév vagy jelszó') 
        return render(request, 'login.html', {'form':form})

def bevitel_kiadas( request):
     bevform = BevitelForm()
     kiform = KiadasForm()
     alapanyagok_lista = Alapanyag.objects.all()               

     if request.method == 'POST':  
        bevform = BevitelForm(request.POST or None)
        kiform = KiadasForm(request.POST or None)
        if 'bevitel' in request.POST:
            if bevform.is_valid():
                if Alapanyag.objects.filter(anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                                            vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                                            meret_valaszt = bevform.cleaned_data['meret_valaszt'],                                         
                                            ).exists():
                    '''Alapanyag.objects.filter(anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                                            vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                                            meret_valaszt = bevform.cleaned_data['meret_valaszt'],).update(darabszam=F('darabszam') + bevform.cleaned_data['darabszam'])'''
                    if bevform.cleaned_data['rogzit_datum'] != Alapanyag.objects.get(anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                                                                                    vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                                                                                    meret_valaszt = bevform.cleaned_data['meret_valaszt'],).rogzit_datum:
                        Alapanyag.objects.filter(anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                                                vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                                                meret_valaszt = bevform.cleaned_data['meret_valaszt'],).update(darabszam=F('darabszam') + bevform.cleaned_data['darabszam'],
                                                                                                        rogzit_datum=bevform.cleaned_data['rogzit_datum'])
                        bevform = BevitelForm()
                        kiform = KiadasForm()
                    else:
                        messages.error(request, f'"{bevform.cleaned_data["anyagtipusa"]}, {bevform.cleaned_data["vastagsag_valaszt"]}, {bevform.cleaned_data["meret_valaszt"]}" ilyen anyag ezekkel a paraméterekkel, már van rögzítve a raktárban!')
                        bevform = BevitelForm()
                        kiform = KiadasForm()
                else:
                    ujanyag = Alapanyag.objects.create(
                        anyagtipusa = bevform.cleaned_data['anyagtipusa'],
                        vastagsag_valaszt = bevform.cleaned_data['vastagsag_valaszt'],
                        meret_valaszt = bevform.cleaned_data['meret_valaszt'],
                        darabszam = bevform.cleaned_data['darabszam'],
                        polc_szama = bevform.cleaned_data['polc_szama'],
                        rogzit_datum = bevform.cleaned_data['rogzit_datum'],)
                    ujanyag.save()
                    bevform = BevitelForm()
                    kiform = KiadasForm()
                    return redirect('raktar')
        elif 'kiad' in request.POST:          
             if kiform.is_valid():
                if Alapanyag.objects.filter(anyagtipusa = kiform.cleaned_data['anyagtipusa'],
                                                vastagsag_valaszt = kiform.cleaned_data['vastagsag_valaszt'],
                                                meret_valaszt = kiform.cleaned_data['meret_valaszt'],                                         
                                                ).exists():
                    Alapanyag.objects.filter(anyagtipusa = kiform.cleaned_data['anyagtipusa'],
                                                vastagsag_valaszt = kiform.cleaned_data['vastagsag_valaszt'],
                                                meret_valaszt = kiform.cleaned_data['meret_valaszt'],).update(darabszam=F('darabszam') - kiform.cleaned_data['darabszam'])
                    
                    kiform = KiadasForm()
                    return redirect('raktar')
     return render(request, 'raktar.html', { 'object_list':alapanyagok_lista,
                                            'bevform': bevform,
                                            'kiform': kiform })

def megrendeles(request):
    megrform = MegrendelesForm()
    megrendelesek_lista = Megrendelesek.objects.all() 
    if request.method == 'POST':
        megrform = MegrendelesForm(request.POST)
        if megrform.is_valid():
            if Megrendelesek.objects.filter(munkalap_szama = megrform.cleaned_data['munkalap_szama']).exists():
               messages.error(request, f'Ezzel a munkalap számmal már van rögzítve megrndelés!!!!!!')
               megrform = MegrendelesForm() 
            else:

                megrform.save()
                megrform = MegrendelesForm()  

    return render(request, 'megrendeles.html', { 'object_list':megrendelesek_lista,
                                            'megrform': megrform})

def logout_page(request):
    logout(request)
    return redirect('login')













