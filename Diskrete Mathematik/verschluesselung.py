import random

import euler

import math


def maxPrimeFactor(n):
    maxPrime = -1

    while n % 2 == 0:
        maxPrime = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

    if n > 2:
        maxPrime = n

    return int(maxPrime)



def symetrische_verschluesselung(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Konvertiere den Buchstaben in einen entsprechenden Integer-Wert (A=0, B=1, usw.)
            char_value = ord(char.upper()) - ord('A')
            # Verschlüssele den Integer-Wert mit dem Verschiebeschlüssel
            encrypted_value = (char_value + shift) % 26
            # Konvertiere den verschlüsselten Integer-Wert zurück in einen Buchstaben
            encrypted_char = chr(encrypted_value + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_encryption(plaintext, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Konvertiere den Buchstaben in einen entsprechenden Integer-Wert (A=0, B=1, usw.)
            char_value = ord(char.upper()) - ord('A')
            # Konvertiere den Buchstaben des Schlüsselworts in einen entsprechenden Integer-Wert
            keyword_char_value = ord(keyword[i % keyword_length]) - ord('A')
            # Verschlüssele den Buchstaben mit dem Schlüsselwort
            encrypted_value = (char_value + keyword_char_value) % 26
            # Konvertiere den verschlüsselten Integer-Wert zurück in einen Buchstaben
            encrypted_char = chr(encrypted_value + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def rsaKeyGen(p, q):
    if not euler.isPrime(p) or not euler.isPrime(q):
        return 'p or q is not prime'
    elif p == q:
        return 'p and q must be different'

    n = p * q

    phiVonN = euler.phi(n)

    # eine teilerfremde zahl kleiner als phiVonN und teilerfremnd zu phiVonN
    while True:
        e = random.randrange(1, phiVonN - 1)
        if euler.ggtfunction(e, phiVonN) == 1:
            break

    # d*e = 1 mod phiVonN
    d = euler.multiplative_inverse(e, phiVonN)
    return (n, e), (n, d)


def rsa_clear_text_benjamin(ciphertext, private_key):
    N, d = private_key
    mapping = {'00': ' ', '01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'F', '07': 'G', '08': 'H',
               '09': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q',
               '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}

    decrypted_message = ""

    for c in ciphertext:
        m = pow(c, d, N)
        print(f"{c}^{d} mod {N} = {m}")

        num_str = str(m).zfill(4)
        num1 = num_str[:2]
        num2 = num_str[2:]
        decrypted_char = mapping[num1] + mapping[num2]

        decrypted_message += decrypted_char

    return decrypted_message
def calculate_ciphertext(message, public_key):
    N, e = public_key
    ciphertext = []

    for char in message:
        # Konvertiere den Buchstaben in einen entsprechenden Integer-Wert (A=0, B=1, usw.)
        m = ord(char.upper()) - ord('A')

        # Verschlüssele den numerischen Wert
        c = pow(m, e, N)

        # Füge den verschlüsselten Wert zur Ergebnisliste hinzu
        ciphertext.append(c)

    return ciphertext


def calculate_private_key(public_key, ciphertext):
    N, e = public_key

    # Chiffrat in numerische Werte umwandeln
    c = ciphertext

    # Totient von N berechnen
    phi = euler.phi(N)

    # Öffentlichen Exponenten e mit dem privaten Exponenten d berechnen
    d = euler.multiplative_inverse(e, phi)

    # Klartext wiederherstellen
    decrypted_message = [pow(char, d, N) for char in c]
    decrypted_message = ''.join(chr(char + ord('A')) for char in decrypted_message)

    return d, decrypted_message


def rsa_decrypt(ciphertext, private_key):
    N, d = private_key

    decrypted_message = ""

    for c in ciphertext:
        # Entschlüsselung des Chiffratwerts mithilfe des privaten Exponenten d
        m = pow(c, d, N)

        # Konvertiere den numerischen Wert in einen Buchstaben
        decrypted_char = chr(m + ord('A'))

        # Füge den entschlüsselten Buchstaben zur Ergebniszeichenkette hinzu
        decrypted_message += decrypted_char

    return decrypted_message


if __name__ == '__main__':
    #plaintext = "FUSSBALLNATIONALMANNSCHAFT"
    #keyword = "MARY"
    cipheratext = [5672, 100, 83, 1403, 5749, 280, 4386]
    print(rsa_clear_text_benjamin(cipheratext, (6161, 2281)))



    #print(vigenere_encryption(plaintext, keyword))
    #
    # prime1 = maxPrimeFactor(453465)
    # print(prime1)
    # prime2 = maxPrimeFactor(233465)
    # print(prime2)
    # publicKey, privateKey = rsaKeyGen(53, 103)
    # print('Public Key:', publicKey)
    # print('Private Key:', privateKey)
    # publicKey = (10033, 23)
    # ciphertext = calculate_ciphertext(plaintext, publicKey)
    # print('Ciphertext:', ciphertext)
    # private_key, decrypted_message_from_private = calculate_private_key(publicKey, ciphertext)
    # print("Privater Exponent:", private_key)
    # print("Entschlüsselte Nachricht:", decrypted_message_from_private)
    # print(rsa_decrypt(ciphertext, privateKey))
