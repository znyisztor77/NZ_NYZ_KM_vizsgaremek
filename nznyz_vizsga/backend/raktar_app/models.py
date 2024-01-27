from django.db import models

# Create your models here.

class Dolgozok(models.Model):
    nev =models.CharField(max_length = 255)
    beosztas_kivalaszt = [(1,"Raktáros"),
                          (2,"Lézervágó")]

    beosztas = models.IntegerField(choices = beosztas_kivalaszt)


    def __str__(self):
        return self.nev
    
class Anyagtipus(models.Model):
     anyagtipus = models.CharField(max_length = 255)
     anyag_kivalaszt = [(1,'Aluminium'),
                         (2, 'Horganyzott'),
                         (3, 'Plexi'),
                         (4, 'Rozsdamentes'),
                         (5, 'Szenacél')]
     anyagtipusa = models.IntegerField(choices = anyag_kivalaszt)

     def __str__(self):
        return self.anyagtipus

    
class Alapanyag(models.Model):
     vastagsag = [(1, "0.5"),
                  (2, "1.0"),
                  (3, "1,5"),
                  (4, "2.0"),
                  (5, "2,5")]
     
     meret_x = [(1, "1000"),
                (2, "1250"),
                (3, "1500"),]
     meret_y = [(1, "2000"),
                (2, "2500"),
                (3, "3000"),]
     aktualiMennyiseg = models.IntegerField()

     anyagtipus = models.ForeignKey(Anyagtipus, on_delete =models.CASCADE ) 
     vastagsag_valaszt = models.IntegerField(choices = vastagsag)
     meret_x_valaszt = models.IntegerField(choices = meret_x) 
     meret_y_valaszt = models.IntegerField(choices = meret_y)       

class Megrendelesek(models.Model):
        dolgozo = models.ForeignKey(Dolgozok, on_delete = models.CASCADE)
        felhasznaltMennyiseg = models.IntegerField()
        datumKezdes = models.DateField()
        datumBefejezes = models.DateField()
        alapanyag = models.ForeignKey(Alapanyag, on_delete = models.CASCADE)

        


