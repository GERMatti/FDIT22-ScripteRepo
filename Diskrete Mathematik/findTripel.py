def findTripel(wert1,wert2,wert3,Gesamtwert):
    count = 0
    xBereich = Gesamtwert // wert1
    yBereich = Gesamtwert // wert2
    zBereich = Gesamtwert // wert3

    for b in range(1, xBereich):  # Der Wertebereich von b basiert auf der maximalen Anzahl der Bücher, die mit dem Budget von Gesamtwert gekauft werden können
        for p in range(1, yBereich):  # Der Wertebereich von p basiert auf der maximalen Anzahl der Pralinenschachteln
            for w in range(1, zBereich):  # Der Wertebereich von w basiert auf der maximalen Anzahl der Weinflaschen
                if wert1 * b + wert2 * p + wert3 * w == Gesamtwert:
                    count += 1
                    print("Tripel " + str(count) + ": " + str(b) + " Bücher, " + str(p) + " Pralinenschachteln, " + str(w) + " Weinflaschen")

    print(count)

if __name__ == '__main__':    
    print(findTripel(5, 3, 2, 100))