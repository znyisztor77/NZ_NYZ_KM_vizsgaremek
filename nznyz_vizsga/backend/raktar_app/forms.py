from django import forms
from .models import Megrendelesek, Alapanyag
from .admin import CustomUser



class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30, widget= forms.PasswordInput)


class BevitelForm(forms.Form):
    DATE_INPUT_FORMATS = ['%Y-%m-%d']

    alapanyagtipusa = Alapanyag.anyagtipus
    anyagtipus = forms.ChoiceField(choices = alapanyagtipusa)
    merete = Alapanyag.meret
    méret = forms.ChoiceField(choices = merete)
    vastagsaga = Alapanyag.vastagsag
    vastagság = forms.ChoiceField(choices = vastagsaga)

    darabszám = forms.IntegerField()
    polc_száma = forms.IntegerField()
    rögzítés_dátum = forms.DateField( widget=forms.DateInput(format = "%Y-%m-%d", attrs={"type": "date"}), input_formats=DATE_INPUT_FORMATS)


class KiadasForm(forms.Form):
    DATE_INPUT_FORMATS = ['%Y-%m-%d']
    alapanyagtipus = Alapanyag.anyagtipus
    #dolgozok = CustomUser.USERNAME_FIELD
    #dolgozo = forms.ChoiceField(choices=dolgozok)
    alapanyagtipusa = Alapanyag.anyagtipus
    anyagtipus = forms.ChoiceField(choices = alapanyagtipusa)
    merete = Alapanyag.meret
    méret = forms.ChoiceField(choices = merete)
    vastagsaga = Alapanyag.vastagsag
    vastagság = forms.ChoiceField(choices = vastagsaga)
    darabszam = forms.IntegerField()
    polc_szama = forms.IntegerField()
    kiadas_datum = forms.DateField(widget=forms.DateInput(format = "%Y-%m-%d", attrs={"type": "date"}), input_formats = DATE_INPUT_FORMATS)
