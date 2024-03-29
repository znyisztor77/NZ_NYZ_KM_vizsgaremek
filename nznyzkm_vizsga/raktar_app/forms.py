from django import forms
from .models import Megrendelesek, Alapanyag
#from .admin import Dolgozo


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30, label="Felhasználónév")
    password = forms.CharField(max_length = 30, label="Jelszó", widget= forms.PasswordInput)


class BevitelForm(forms.ModelForm):

    class Meta:
        DATE_FORMATS = ['%Y-%m-%d']
        model = Alapanyag
        fields = ('anyagtipusa',
                  'vastagsag_valaszt',
                  'meret_valaszt',
                  'darabszam',
                  'polc_szama',
                  'rogzit_datum' )
        widgets={'rogzit_datum': forms.DateInput(attrs={"type": "date"}, format = "%Y-%m-%d" )}


class KiadasForm(forms.ModelForm):

    class Meta:
        DATE_FORMATS = ['%Y-%m-%d']
        model = Alapanyag
        fields = ('anyagtipusa',
                  'vastagsag_valaszt',
                  'meret_valaszt',
                  'darabszam',)
       

class MegrendelesForm(forms.ModelForm):

    class Meta:
        model = Megrendelesek
        fields = ('munkalap_szama',
                  'dolgozo',
                  'alapanyag',
                  'datumKezdes',
                  'datumBefejezes',
                  'felhasznaltMennyiseg')
        widgets={'datumKezdes': forms.DateInput(attrs={"type": "date"},format = "%Y-%m-%d" ), 
                 'datumBefejezes': forms.DateInput(attrs={"type": "date"}, format = "%Y-%m-%d" )}
        
        labels = {
        'munkalap_szama': 'Munkalap száma',
        'dolgozo': 'Dolgozó',
        'alapanyag': 'Alapanyag',
        'datumKezdes': 'Dátum kezdés',
        'datumBefejezes': 'Dátum befejezés',
        'felhasznaltMennyiseg': 'Felhasznált mennyiség'
    }