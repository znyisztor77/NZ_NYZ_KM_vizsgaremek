# NZ_NYZviszga
Német Zoltán Nyisztor Zoltán Vizsgaremek dokumentáció 

 

Az általunk készített alkalmazás egy lézer vágó cég raktár kezelését végzi, amelyben a raktárban tárolt alapanyagokat(különböző anyag típusok) és a megrendeléseket nyilván tartását végzi.
Az alkalmazásban nyomon követhető, hogy egy anyagot jelen esetbe egy lemez táblát a melyik dolgozó használta fel és melyik megrendeléshez. 
Az alkalmazás webes felhasználó felületű, amely a  Django Framework segítségével van megoldva. 
A webes felület tartalmaz egy qr kódot amely segítségével telefonon is kezelhető a felület. 

Django framework: https://www.djangoproject.com/ 

A Django Framework kezeli az Mysql adatbázist és segítségével van megjelenítve a webes kezelő felület. 
A adatbázist a XAMPP laklamazás kezeli.

XAMPP mysql webserver: https://www.apachefriends.org/hu/index.html

A felhasználói felület és az adtbázis közötti kapcsolatot a XAMPP alkalmazás biztosítja a Django Framework-ön keresztül. 

A webes kezelő felület html, css fájlokból tevődik össze. Az sql adatbázis kapcsolatot pedig a django framework biztosítja. 

---
A legelső oldal egy bejelentkező form.
Szükséges megadni a nevet é jelszőt.
A főoldal aszerint töltődik be, hogy ki fogja használni az alkalmazást.
Raktáros oldal:
 feladatköre:
  - anyag kiadása
  - új anyagok hozzáadása
  - 

