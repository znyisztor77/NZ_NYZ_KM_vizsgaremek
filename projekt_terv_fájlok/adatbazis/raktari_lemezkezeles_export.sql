-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2023. Nov 15. 17:51
-- Kiszolgáló verziója: 10.4.28-MariaDB
-- PHP verzió: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `raktari_lemezkezeles`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `alapanyagok`
--

CREATE TABLE `alapanyagok` (
  `alapanyag_id` int(11) NOT NULL,
  `anyagtipus_id` int(11) DEFAULT NULL,
  `vastagsag` enum('0.5','0.8','1.0','1.2','1.5','2.0','2.5','3.0','4.0','5.0','6.0','8.0','10.0','12.0','15.0','20.0') DEFAULT NULL,
  `meret_x` int(11) DEFAULT NULL,
  `meret_y` int(11) DEFAULT NULL,
  `akt_mennyiseg` int(11) DEFAULT NULL,
  `datum_be` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `alapanyagok`
--

INSERT INTO `alapanyagok` (`alapanyag_id`, `anyagtipus_id`, `vastagsag`, `meret_x`, `meret_y`, `akt_mennyiseg`, `datum_be`) VALUES
(1, 1, '0.5', 3000, 1500, 5, '2023-11-04'),
(2, 2, '0.5', 2000, 1000, 4, '2023-11-04'),
(3, 3, '6.0', 2000, 1000, 10, '2023-11-05'),
(4, 4, '10.0', 2500, 1250, 10, '2023-11-05'),
(5, 5, '8.0', 2500, 1250, 6, '2023-11-05');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `anyagtipus`
--

CREATE TABLE `anyagtipus` (
  `anyagtipus_id` int(11) NOT NULL,
  `anyagtipus` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `anyagtipus`
--

INSERT INTO `anyagtipus` (`anyagtipus_id`, `anyagtipus`) VALUES
(1, 'aluminium'),
(2, 'horganyzott'),
(3, 'plexi'),
(4, 'rozsdamentes'),
(5, 'szenacel');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `dolgozok`
--

CREATE TABLE `dolgozok` (
  `dolgozo_id` int(11) NOT NULL,
  `nev` varchar(255) DEFAULT NULL,
  `beosztas` enum('raktaros','lezervago') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `dolgozok`
--

INSERT INTO `dolgozok` (`dolgozo_id`, `nev`, `beosztas`) VALUES
(1, 'Takács Béla', 'raktaros'),
(2, 'Kovács József', 'lezervago'),
(3, 'Horváth Rudolf', 'lezervago'),
(4, 'Szabó Roland', 'raktaros'),
(5, 'Lakatos Imre', 'lezervago');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `megrendelesek`
--

CREATE TABLE `megrendelesek` (
  `munka_id` int(11) NOT NULL,
  `felhaszn_menny` int(11) DEFAULT NULL,
  `dolgozo_id` int(11) DEFAULT NULL,
  `datum_kezd` date DEFAULT NULL,
  `datum_bef` date DEFAULT NULL,
  `alapanyag_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `megrendelesek`
--

INSERT INTO `megrendelesek` (`munka_id`, `felhaszn_menny`, `dolgozo_id`, `datum_kezd`, `datum_bef`, `alapanyag_id`) VALUES
(1, 1, 2, '2023-11-04', '2023-11-05', 4),
(2, 1, 3, '2023-11-04', '2023-11-05', 5),
(3, 1, 5, '2023-11-04', '2023-11-05', 2),
(4, 1, 4, '2023-11-04', '2023-11-05', 1),
(5, 1, 1, '2023-11-04', '2023-11-05', 3);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `alapanyagok`
--
ALTER TABLE `alapanyagok`
  ADD PRIMARY KEY (`alapanyag_id`),
  ADD KEY `anyagtipus_id` (`anyagtipus_id`);

--
-- A tábla indexei `anyagtipus`
--
ALTER TABLE `anyagtipus`
  ADD PRIMARY KEY (`anyagtipus_id`);

--
-- A tábla indexei `dolgozok`
--
ALTER TABLE `dolgozok`
  ADD PRIMARY KEY (`dolgozo_id`);

--
-- A tábla indexei `megrendelesek`
--
ALTER TABLE `megrendelesek`
  ADD PRIMARY KEY (`munka_id`),
  ADD KEY `dolgozo_id` (`dolgozo_id`),
  ADD KEY `alapanyag_id` (`alapanyag_id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `alapanyagok`
--
ALTER TABLE `alapanyagok`
  MODIFY `alapanyag_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT a táblához `anyagtipus`
--
ALTER TABLE `anyagtipus`
  MODIFY `anyagtipus_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT a táblához `dolgozok`
--
ALTER TABLE `dolgozok`
  MODIFY `dolgozo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT a táblához `megrendelesek`
--
ALTER TABLE `megrendelesek`
  MODIFY `munka_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `alapanyagok`
--
ALTER TABLE `alapanyagok`
  ADD CONSTRAINT `alapanyagok_ibfk_1` FOREIGN KEY (`anyagtipus_id`) REFERENCES `anyagtipus` (`anyagtipus_id`);

--
-- Megkötések a táblához `megrendelesek`
--
ALTER TABLE `megrendelesek`
  ADD CONSTRAINT `megrendelesek_ibfk_1` FOREIGN KEY (`dolgozo_id`) REFERENCES `dolgozok` (`dolgozo_id`),
  ADD CONSTRAINT `megrendelesek_ibfk_2` FOREIGN KEY (`alapanyag_id`) REFERENCES `alapanyagok` (`alapanyag_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
