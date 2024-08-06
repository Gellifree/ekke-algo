# Beadandó tervezése

## Keresési függvények elemzése és összehasonlítása

Tesztelni kívánt függények listája:
- Lineáris keresés
- Strázsás keresés
- Lineáris keresés rendezett sorozatban
- Bináris keresés

## Első lépések

Ahoz, hogy a jövőben egyszerűbbé tegyem az elkészült alkalmazás használatát, az első elkészített modul, egy menü kirajzolásáért felelős osztály. Ez a gyakorlatban a felhasználónak könnyen értelmezhető formátumban opciókat ad, amivel könnyen navigálhatunk különböző funkciók között. A menü könnyen bővíthető és hibabiztos.

A következő lépés, hogy számbavegyük hogy milyen szoftver modulokra van szükségünk, és ezeknek milyen kapcsolata van egymással. Szükségünk van a mérési eredmények lementésére, hogy azokat felhasználhassuk a későbbiekben. Ehhez egy lokális SQlite adatbázist tartok a legegyszerűbb megoldásnak.