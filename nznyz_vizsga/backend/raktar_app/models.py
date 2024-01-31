from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Dolgozok(models.Model):
    nev =models.CharField(max_length = 255)
    beosztas_kivalaszt = [(1,"Raktáros"),
                          (2,"Lézervágó")]

    beosztas = models.IntegerField(choices = beosztas_kivalaszt)


    def __str__(self):
        return self.nev
    
'''class Anyagtipus(models.Model):
     anyagtipus = models.CharField(max_length = 255)
     anyag_kivalaszt = [(1,'Aluminium'),
                        (2, 'Horganyzott'),
                        (3, 'Plexi'),
                        (4, 'Rozsdamentes'),
                        (5, 'Szenacél')]
     anyagtipusa = models.IntegerField(choices = anyag_kivalaszt)

     anyag_kivalaszt2 = [
                        ("Aluminium" , "Aluminium"),
                        ("Horgganyzott" , "Horganyzott"),
                        ("Plexi", "Plexi"),
                        ("Rozsdamentes","Rozsdamentes"),
                        ("Szénacél", "Szénacél") ]
     anyagtipusa2= models.CharField(max_length = 20 ,choices = anyag_kivalaszt2)

     def __str__(self):
        return self.anyagtipusa2 '''

    
class Alapanyag(models.Model):
     #anyagtipus = models.ForeignKey(Anyagtipus, on_delete =models.CASCADE )
     anyagtipus = [
                        ("Aluminium" , "Aluminium"),
                        ("Horgganyzott" , "Horganyzott"),
                        ("Plexi", "Plexi"),
                        ("Rozsdamentes","Rozsdamentes"),
                        ("Szénacél", "Szénacél") ]
     anyagtipusa= models.CharField(max_length = 20 ,choices = anyagtipus) 

     vastagsag = [(1, "0.5"),
                  (2, "1.0"),
                  (3, "1,5"),
                  (4, "2.0"),
                  (5, "2,5")]
     vastagsag_valaszt = models.IntegerField(choices = vastagsag)
     
     meret_x = [(1, "1000"),
                (2, "1250"),
                (3, "1500"),]
     meret_x_valaszt = models.IntegerField(choices = meret_x)

     meret_y = [(1, "2000"),
                (2, "2500"),
                (3, "3000"),]
     meret_y_valaszt = models.IntegerField(choices = meret_y)       
     keszleten = models.PositiveIntegerField(default=0)
     #keszleten = models.IntegerField()

     '''def __str__(self):
        return self.anyagtipus'''

class Megrendelesek(models.Model):
        munka_id = models.IntegerField()
        felhasznaltMennyiseg = models.IntegerField()
        dolgozo = models.ForeignKey(Dolgozok, on_delete = models.CASCADE)
        datumKezdes = models.DateField()
        datumBefejezes = models.DateField()
        alapanyag = models.ForeignKey(Alapanyag, on_delete = models.CASCADE)

        


