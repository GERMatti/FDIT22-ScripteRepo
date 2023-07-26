def berechne_erwartungswert_einer_stichprobe(werte):
    erwartungswert = sum(werte)
    erwartungswert = float(erwartungswert)
    erwartungswert /= len(werte)
    return erwartungswert

def berechne_varianz_einer_stichprobe(werte):
    erwartungswert = berechne_erwartungswert_einer_stichprobe(werte)
    varianz = 0
    for w in werte:
        varianz += (w - erwartungswert) ** 2
    varianz /= len(werte) - 1
    return varianz

print(10 / 34 * 10 / 34 + 6 / 34 * 6 / 34 + 18 / 34 * 18 / 34)

stichprobenwerte = [192,178,182,150,164,175,186,186,169,174]
print(berechne_erwartungswert_einer_stichprobe(stichprobenwerte))
print(berechne_varianz_einer_stichprobe(stichprobenwerte))
