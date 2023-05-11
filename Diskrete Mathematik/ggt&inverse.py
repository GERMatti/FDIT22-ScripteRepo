def ggt(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def erweiterter_ggt(a, b):
    """Berechnet den größten gemeinsamen Teiler zweier Zahlen a und b
    und gibt zusätzlich die Koeffizienten s und t zurück, so dass
    s*a + t*b = ggt(a,b) gilt."""
    if a == 0:
        return b, 0, 1
    else:
        ggt, s, t = erweiterter_ggt(b % a, a)
        return ggt, t - (b // a) * s, s

def multiplative_inverse(a, b):
    ggt, s, _ = erweiterter_ggt(a, b)
    if ggt != 1:
        return None
    else:
        return s % b
    

if __name__ == '__main__':
    #Hier können eigene Tests eingefügt werden
    print(ggt(12, 8))
    print(erweiterter_ggt(12, 8))
    print(multiplative_inverse(12, 8))