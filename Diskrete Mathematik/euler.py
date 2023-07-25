import random
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


def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


if __name__ == '__main__':
    # Beispielaufruf des Algorithmus mit der Eingabevariablen 10
    n = 1400
    phi_value = phi(n)
    print("Eulersche Phi-Funktion für", n, ":", phi_value)

    print(ggtfunction(19, 54))
    print(erweiterter_ggt(19, 54))
    print(multiplative_inverse(19, 54))
    print(is_Prime(8597))
    print(4**4792 % 4793)