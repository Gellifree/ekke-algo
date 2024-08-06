# Adatszerkezet és algoritmusok Gyakorlat beadandó feladat

![Kovács Norbert - PTI BSC](./Github_Header.png)

## Beadandó feladatok rövid leírása

- Kereső függvények elemzése és összehasonlítása (20 oldal)
- Rendező algoritmusok elemzése és összehasonlítása (20 oldal)

## Megoldás tervezése / célok

A célom hogy elkészítsek egy olyan csomagot (esetünkben egyszerűen csak *analyzer* néven), amely képes elvégezni a kereső, és rendező algoritmusok elemzését. Az első beadandó keretein belül fogom megtervezni és elkészíteni ezt a csomagot, mégpedig úgy hogy az alkalmas legyen rugalmas **mérések** elvégzésére. Ez alatt azt értem, hogy különböző hosszúságú sorozatokon, meghatározott ismétlésszámmal képesek legyünk különböző függvényeket futtatni. Hasonló tesztelésre alkalmas csomagok biztosan léteznek, azonban ezesetben ezt saját magam szeretném elkészíteni. Az alkalmazás felé igényem, hogy olyan rugalmas legyen hogy képes legyen mind az első (keresési függvények) és a második beadandó feladat (rendezések) elemzésére is. A gyűjtött mérési eredményeket olyan formában kívánom strukturálni, ami később felhasználható az összehasonlítási folyamatokhoz. Erre a legegyszerűbb módszert az SQlite lokális adatbázis létrehozása biztosítja. A gyakorlati mérések elvégézése mellett, szeretném megérteni a kapott statisztikai eredményeket, és esetleg valamilyen konklúziót is levonni, vagy mintákat felismerni. Azonban a feladat egyszerű elméleti mivolta miatt nem számítok túlságosan érdekes következtetésekre.

Összességében egy olyan csomagot akarok létrehozni, ami képes különböző Python függvények futási idejének mérésére. Természetesen esetünkben sok előkészítés kell hogy akár a keresést is mérni tudjuk. Különböző stratégiáimat is részletesen elemzem majd a beadandó keretein belül.

### Használt eszközök

| Feladat | Eszköz |
|---|---|
| Beadandó PDF (dokumentáció) | LateX |
| Grafikák / ábrák készítése | Figma / Inkscape |
| Grafikonok / statisztikák vizualizálása | Matplotlib |
| Verziókezelés | Github |
| Programozási nyelv | Python 3 |

## Segédlet

Unit tesztek futtatása a src/ könyvtárból: `py -m unittest -v`
