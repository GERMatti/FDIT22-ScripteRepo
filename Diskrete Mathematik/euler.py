def faktorisiere_in_primzahlen(zahl):
    faktoren = []
    teiler = 2

    while teiler <= zahl:
        if zahl % teiler == 0:
            faktoren.append(teiler)
            zahl = zahl / teiler
        else:
            teiler += 1

    if len(faktoren) == 2:
        return faktoren
    else:
        return None

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0 and i != n:
            return False
    return True

def ggtfunction(a, b):
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

def modulare_exponentiation(a, b, n):
    """Berechnet a^b mod n"""
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        b = b // 2
        a = (a * a) % n
    return result

def phi(n):
    count = 0
    for i in range(1, n+1):
        if ggtfunction(n, i) == 1:
            count += 1
    return count

if __name__ == '__main__':    
    # Beispielaufruf des Algorithmus mit der Eingabevariablen 10
    n = 10
    phi_value = phi(n)
    print("Eulersche Phi-Funktion für", n, ":", phi_value)

    print(ggtfunction(12, 8))
    print(erweiterter_ggt(12, 8))
    print(multiplative_inverse(12, 8))