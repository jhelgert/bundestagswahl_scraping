Ein simpler Scraper, der die feingliedrigen Wahlbezirksergebnisse der Bundestagswahl 2021
basierend auf [https://wahlen.votemanager.de/](https://wahlen.votemanager.de/)
*scraped*. Warum? [Darum!](https://www.bundeswahlleiter.de/bundestagswahlen/2021/ergebnisse/opendata.html#c32edb46-be42-4cc7-bfea-07a0f639a2da).

Benötigte Libraries:

``` python
pip3 install tqdm requests bs4 pandas
```

Hinweise:
- **Die Daten sind leider nicht vollständig, da einige Gemeinden bzw. Bundesländer (Hamburg, Berlin, Rheinland-Pfalz, Thüringen, Saarland, Brandenburg) einen anderen Dienstleister verwenden**.
- Zudem sind einige Server von bestimmten Kommunen offline...
- Für das *Scrapen* der Behörden kann leider nur ein Thread verwendet werden,
da man sonst schnell als Bot erkannt wird. Selbiges gilt aber nicht für
das *Scrapen* der Wahlbezirke, da diese von unterschiedlichen Servern
abgefragt werden.

Ein PR für die restlichen Bundesländer ist mehr als willkommen! :)

# Auswertung

Hier jeweils die 5 besten Wahlbezirke der großen Parteien:

## FDP

|       | Bundesland        | Stadt             | Wahlbezirk                       |   CDU |   SPD |  AfD |   FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :---------------- | :---------------- | :------------------------------- | ----: | ----: | ---: | ----: | ----: | --------: | ---: |
| 17576 | Hessen            | Frankfurt am Main | 924-02                           |  17.7 |     5 |  5.8 |  37.6 |  19.8 |         6 |  nan |
| 11942 | Hessen            | Diemelsee         | OT Sudeck, Dorfgemeinschaftshaus | 26.92 | 15.38 | 14.1 |  35.9 |   nan |       nan |  nan |
| 55466 | Baden-Württemberg | Stuttgart         | 001-51 VWA Haus                  |  22.7 |  11.7 |  3.4 |  34.4 |  23.4 |       2.1 |  nan |
| 51617 | Baden-Württemberg | Schriesheim       | 110 Heinrich-Sigmund-Gymnasium   | 23.87 | 14.84 |  nan | 34.19 | 15.48 |       nan |  nan |
| 17119 | Hessen            | Frankfurt am Main | 162-05                           |  23.6 |    14 |  2.1 |  33.5 |    18 |       2.3 |  nan |

## CDU

|       | Bundesland          | Stadt         | Wahlbezirk      |   CDU |   SPD |  AfD |  FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :------------------ | :------------ | :-------------- | ----: | ----: | ---: | ---: | ----: | --------: | ---: |
| 36859 | Niedersachsen       | Spelle        | 0010 DGH Heitel | 72.12 | 10.58 | 5.77 | 6.73 |  1.92 |      0.96 |  nan |
| 53779 | Niedersachsen       | Spelle        | 0010 DGH Heitel | 72.12 | 10.58 | 5.77 | 6.73 |  1.92 |      0.96 |  nan |
| 50743 | Niedersachsen       | Spelle        | 0010 DGH Heitel | 72.12 | 10.58 | 5.77 | 6.73 |  1.92 |      0.96 |  nan |
| 53795 | Niedersachsen       | Spelle        | 0010 DGH Heitel | 72.12 | 10.58 | 5.77 | 6.73 |  1.92 |      0.96 |  nan |
| 51132 | Nordrhein-Westfalen | Schmallenberg | Rarbach         | 70.62 | 11.86 | 2.06 | 7.22 |  3.61 |      0.52 |  nan |

## CSU

|       | Bundesland | Stadt          | Wahlbezirk    |  CDU |   SPD |  AfD |  FDP | GRÜNE | DIE LINKE |   CSU |
| ----: | :--------- | :------------- | :------------ | ---: | ----: | ---: | ---: | ----: | --------: | ----: |
| 18950 | Bayern     | Gaukönigshofen | Eichelsee     |  nan |  6.49 |  nan |  2.6 |  7.79 |       nan | 71.43 |
| 54612 | Bayern     | Steinwiesen    | Neufang       |  nan |  8.89 |  6.3 |  nan |   nan |       nan | 66.67 |
| 29678 | Bayern     | Karlstadt      | Stadelhofen   |  nan |  5.88 |  nan | 7.35 |  5.88 |       nan | 66.18 |
| 54614 | Bayern     | Steinwiesen    | Nurn          |  nan |  9.03 | 5.56 |  nan |   nan |       nan | 63.89 |
| 15357 | Bayern     | Ensdorf        | 0003 Thanheim |  nan | 10.81 |  2.7 |  nan |     0 |       nan | 63.51 |

## SPD

|       | Bundesland    | Stadt              | Wahlbezirk                      |   CDU |   SPD |  AfD |  FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :------------ | :----------------- | :------------------------------ | ----: | ----: | ---: | ---: | ----: | --------: | ---: |
| 32046 | Niedersachsen | Krummhörn          | Hamswehrum                      | 11.63 | 62.79 |  nan | 6.98 |  8.37 |       nan |  nan |
| 26019 | Hessen        | Hessisch Lichtenau | Hopfelde                        |  9.48 | 62.07 | 1.72 | 8.62 |  8.62 |      4.31 |  nan |
| 22500 | Hessen        | Haina (Kloster)    | 00020 - Battenhausen/Hüttenrode |  10.1 | 61.62 | 6.06 | 7.07 |  8.08 |      2.02 |  nan |
| 32054 | Niedersachsen | Krummhörn          | Visquard                        |  12.5 |  60.9 |  nan | 8.33 |  7.05 |       nan |  nan |
| 12580 | Niedersachsen | Dornum             | Schwittersum                    | 19.82 | 60.35 | 5.29 | 4.85 |  6.17 |      0.88 |  nan |

## Grüne

|       | Bundesland          | Stadt                | Wahlbezirk              |  CDU |   SPD |  AfD |  FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :------------------ | :------------------- | :---------------------- | ---: | ----: | ---: | ---: | ----: | --------: | ---: |
| 17946 | Baden-Württemberg   | Freiburg im Breisgau | 901-05                  |  2.8 |  11.3 |  0.2 |  1.9 |  65.7 |      11.8 |  nan |
| 17842 | Baden-Württemberg   | Freiburg im Breisgau | 680-03                  |  2.9 |  11.5 |  1.8 |  3.3 |  60.4 |      12.3 |  nan |
| 17944 | Baden-Württemberg   | Freiburg im Breisgau | 901-03                  |  4.1 |  13.6 |  0.7 |    6 |  59.8 |       9.7 |  nan |
| 40555 | Nordrhein-Westfalen | Münster              | 93002 - Brief Sentrup 2 | 7.45 | 13.38 |  nan | 8.69 |  57.1 |       6.9 |  nan |
| 17803 | Baden-Württemberg   | Freiburg im Breisgau | 531-02                  |  2.7 |  14.2 |  3.4 |  7.1 |  55.3 |       9.5 |  nan |

## AfD

|       | Bundesland     | Stadt      | Wahlbezirk                            |   CDU |   SPD |   AfD |  FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :------------- | :--------- | :------------------------------------ | ----: | ----: | ----: | ---: | ----: | --------: | ---: |
| 37677 | Sachsen        | Marienberg | Multifunktionszentrum Rübenau         | 11.43 |  9.87 | 55.38 |  7.4 |   nan |       nan |  nan |
|  1066 | Sachsen-Anhalt | Güsten     | 012 Schützenhaus Plötzkau, OT Bründel | 11.43 | 15.24 | 50.48 |  nan |   nan |      2.86 |  nan |
| 28375 | Sachsen-Anhalt | Güsten     | 012 Schützenhaus Plötzkau, OT Bründel | 11.43 | 15.24 | 50.48 |  nan |   nan |      2.86 |  nan |
| 50069 | Sachsen-Anhalt | Güsten     | 012 Schützenhaus Plötzkau, OT Bründel | 11.43 | 15.24 | 50.48 |  nan |   nan |      2.86 |  nan |
| 19783 | Sachsen-Anhalt | Güsten     | 012 Schützenhaus Plötzkau, OT Bründel | 11.43 | 15.24 | 50.48 |  nan |   nan |      2.86 |  nan |


## Die Linke

|       | Bundesland | Stadt   | Wahlbezirk |  CDU |  SPD |  AfD |  FDP | GRÜNE | DIE LINKE |  CSU |
| ----: | :--------- | :------ | ---------: | ---: | ---: | ---: | ---: | ----: | --------: | ---: |
| 34389 | Sachsen    | Leipzig |       2119 |  2.9 | 11.4 |  5.6 |  3.9 |  21.2 |      45.7 |  nan |
| 34382 | Sachsen    | Leipzig |       2019 |  2.3 |  8.2 |  5.8 |  3.9 |  30.9 |      42.5 |  nan |
| 34753 | Sachsen    | Leipzig |       2105 |  2.7 |  9.3 |    2 |    4 |  33.6 |        41 |  nan |
| 34502 | Sachsen    | Leipzig |       4131 |  5.3 | 13.8 |  5.3 |  3.5 |  23.6 |      38.2 |  nan |
| 34504 | Sachsen    | Leipzig |       4139 |  5.6 | 11.8 |  4.9 |  3.2 |    28 |      37.7 |  nan |
