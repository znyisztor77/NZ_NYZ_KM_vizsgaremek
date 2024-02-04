from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30, widget= forms.PasswordInput)


class BevitelForm(forms.Form):
    anyagtipus = forms.CharField(max_length = 30)
    méret = forms.CharField(max_length=30)
    vastagság = forms.CharField(max_length=30)
    darabszám = forms.IntegerField()
    polc_száma = forms.IntegerField()
    bevétel_dátum = forms.DateField()


class KiadasForm(forms.Form):
    dolgozo = forms.CharField(max_length = 30)
    anyagtipus = forms.CharField(max_length = 30)
    meret = forms.CharField(max_length=30)
    vastagsag = forms.CharField(max_length=30)
    darabszam = forms.IntegerField()
    polc_szama = forms.IntegerField()
    kiadas_datum = forms.DateField()
