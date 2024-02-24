CREATE DATABASE IF NOT EXISTS `raktari_lemezkezeles`  DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;
USE `raktari_lemezkezeles`;


CREATE TABLE `dolgozok` ( 
`dolgozo_id` INT NOT NULL AUTO_INCREMENT, 
`nev` VARCHAR(255), 
`beosztas` ENUM("raktaros","lezervago"),
PRIMARY KEY(dolgozo_id)
);

CREATE TABLE `anyagtipus`(
`anyagtipus_id` INT NOT NULL AUTO_INCREMENT,
`anyagtipus` VARCHAR(255),
PRIMARY KEY(anyagtipus_id)
);

CREATE TABLE `alapanyagok`(
`alapanyag_id` INT NOT NULL AUTO_INCREMENT,
`anyagtipus_id` INT,
`vastagsag` ENUM("0.5","0.8","1.0","1.2","1.5","2.0","2.5","3.0","4.0","5.0","6.0","8.0","10.0","12.0","15.0","20.0"),
`meret_x` INT,
`meret_y` INT,
`akt_mennyiseg` INT,
`datum_be` DATE,
PRIMARY KEY(alapanyag_id),
FOREIGN KEY(`anyagtipus_id`) REFERENCES `anyagtipus`(`anyagtipus_id`)
);

CREATE TABLE `megrendelesek`(
`munka_id` INT NOT NULL AUTO_INCREMENT,
`felhaszn_menny` INT,
`dolgozo_id` INT,
`datum_kezd` DATE,
`datum_bef` DATE,
`alapanyag_id` INT, 
PRIMARY KEY(munka_id),
FOREIGN KEY(dolgozo_id) REFERENCES `dolgozok`(dolgozo_id),
FOREIGN KEY(alapanyag_id) REFERENCES `alapanyagok`(alapanyag_id)
);








