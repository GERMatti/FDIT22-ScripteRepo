def urne_wahrscheinlichkeiten(urne):
    anzahl_kugeln = sum(urne.values())
    wahrscheinlichkeiten = {}

    for farbe, anzahl in urne.items():
        wahrscheinlichkeiten[farbe] = anzahl / anzahl_kugeln

    return wahrscheinlichkeiten

urne = {'rot': 7, 'grün': 3}
ergebnis = urne_wahrscheinlichkeiten(urne)
print(ergebnis)
