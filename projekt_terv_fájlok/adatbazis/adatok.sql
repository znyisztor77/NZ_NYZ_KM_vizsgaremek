/*Anyagtipus táblába:*/
INSERT INTO `anyagtipus`(`anyagtipus_id`,`anyagtipus`) VALUES ('1','aluminium');
INSERT INTO `anyagtipus`(`anyagtipus_id`,`anyagtipus`) VALUES ('2','horganyzott');
INSERT INTO `anyagtipus`(`anyagtipus_id`,`anyagtipus`) VALUES ('3','plexi');
INSERT INTO `anyagtipus`(`anyagtipus_id`,`anyagtipus`) VALUES ('4','rozsdamentes');
INSERT INTO `anyagtipus`(`anyagtipus_id`,`anyagtipus`) VALUES ('5','szenacel');


/*Dolgozók táblába:*/
INSERT INTO `dolgozok` (`dolgozo_id`,`nev`,`beosztas`) VALUES ('1','Takács Béla','raktaros');
INSERT INTO `dolgozok` (`dolgozo_id`,`nev`,`beosztas`) VALUES ('2','Kovács József','lezervago');
INSERT INTO `dolgozok` (`dolgozo_id`,`nev`,`beosztas`) VALUES ('3','Horváth Rudolf','lezervago');
INSERT INTO `dolgozok` (`dolgozo_id`,`nev`,`beosztas`) VALUES ('4','Szabó Roland','raktaros');
INSERT INTO `dolgozok` (`dolgozo_id`,`nev`,`beosztas`) VALUES ('5','Lakatos Imre','lezervago');


/*Alapanyagok tábla:*/
INSERT INTO `alapanyagok`(`anyagtipus_id`,`vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES ('1','0.5','3000','1500','5','2023-11-04');
INSERT INTO `alapanyagok`(`anyagtipus_id`,`vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES ('2','0.5','2000','1000','4','2023-11-04');
INSERT INTO `alapanyagok`(`anyagtipus_id`,`vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES ('3','6.0','2000','1000','10','2023-11-05');
INSERT INTO `alapanyagok`(`anyagtipus_id`,`vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES ('4','10.0','2500','1250','10','2023-11-05');
INSERT INTO `alapanyagok`(`anyagtipus_id`,`vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES ('5','8.0','2500','1250','6','2023-11-05');

/*Megrendelés tábla:*/
INSERT INTO `megrendelesek`(`munka_id`,`felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) 
VALUES ('1','1','2','2023-11-04','2023-11-05','4'); #(Kovács József,plexi, 10.0,2500x1250)
INSERT INTO `megrendelesek`(`munka_id`, `felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) 
VALUES ('2','1','3','2023-11-04','2023-11-05','5'); #(Horváth Rudolf, rozsdamentes, 8.0, 2500x1250)
INSERT INTO `megrendelesek`(`munka_id`, `felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) 
VALUES ('3','1','5','2023-11-04','2023-11-05','2'); #(Lakatos Imre, aluminium, 0.5, 2000x1000)
INSERT INTO `megrendelesek`(`munka_id`, `felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) 
VALUES ('4','1','4','2023-11-04','2023-11-05','1'); #(Szabo Roland, aluminium, 0.5, 3000x1500)
INSERT INTO `megrendelesek`(`munka_id`, `felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) 
VALUES ('5','1','1','2023-11-04','2023-11-05','3'); #(Takács Béla, szenacel 6.0, 2000x1000)


