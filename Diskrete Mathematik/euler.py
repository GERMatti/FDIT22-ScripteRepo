def ggt(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_phi(n):
    count = 0
    for i in range(1, n+1):
        if ggt(n, i) == 1:
            count += 1
    return count

if __name__ == '__main__':    
    # Beispielaufruf des Algorithmus mit der Eingabevariablen 10
    n = 10
    phi_value = euler_phi(n)
    print("Eulersche Phi-Funktion für", n, ":", phi_value)