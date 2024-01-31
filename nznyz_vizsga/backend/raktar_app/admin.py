from django.contrib import admin
from .models import Dolgozok, Alapanyag, Megrendelesek
#Anyagtipus

# Register your models here.
admin.site.register(Dolgozok)
admin.site.register(Alapanyag)
#admin.site.register(Anyagtipus)
admin.site.register(Megrendelesek)