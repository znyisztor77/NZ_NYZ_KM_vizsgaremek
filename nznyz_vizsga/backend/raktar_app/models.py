from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
     raktaros = models.BooleanField(default=False)
     lezervago = models.BooleanField(default=False)
     

'''class Dolgozok(models.Model):
    nev = models.OneToOneField(User, on_delete= models.CASCADE)
    #nev =models.CharField(max_length = 255)
    beosztas_kivalaszt = [("Raktáros","raktar"),
                          ("Lézervágó","lezervago")]

    beosztas = models.CharField(max_length = 30,  choices = beosztas_kivalaszt)
    raktaros = models.BooleanField(default=False)
    lezervago = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nev.username} {self.beosztas}'''
    
    
class Alapanyag(models.Model):
     anyagtipus = [
                        ("Aluminium" , "Aluminium"),
                        ("Horganyzott" , "Horganyzott"),
                        ("Plexi", "Plexi"),
                        ("Rozsdamentes","Rozsdamentes"),
                        ("Szénacél", "Szénacél") ]
     anyagtipusa= models.CharField(max_length = 20 ,choices = anyagtipus) 
     
     vastagsag = [("0.5", "0.5"),
                  ("1.0", "1.0"),
                  ("1,5", "1,5"),
                  ("2.0", "2.0"),
                  ("2,5", "2,5")]
     vastagsag_valaszt = models.CharField(max_length = 10, choices = vastagsag)
     
     meret = [("1000X2000", "1000X2000"),
              ("1250X2500", "1250X2000"),
              ("1500X3000", "1500X3000"),
              ]
     meret_valaszt = models.CharField(max_length =30, choices = meret)  
     darabszam = models.PositiveIntegerField(default=0)
     polc_szama = models.PositiveIntegerField(default=0)
     rogzit_datum = models.DateField()
     

     def __str__(self):
        return f"{self.anyagtipusa} {self.meret_valaszt} {self.vastagsag_valaszt}"

class Megrendelesek(models.Model):
        
        munkalap_szama = models.CharField(max_length = 30)
        dolgozo = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
        alapanyag = models.ForeignKey(Alapanyag ,on_delete = models.CASCADE)
        datumKezdes = models.DateField()
        datumBefejezes = models.DateField()
        felhasznaltMennyiseg = models.PositiveIntegerField(default=0)
