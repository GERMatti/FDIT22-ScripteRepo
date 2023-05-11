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

if __name__ == '__main__':
    plaintext = "AVEYRON"
    keyword = "FRZ"
    encrypted_text = vigenere_encryption(plaintext, keyword)
    print("Verschlüsselter Text:", encrypted_text)