def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def otp_encrypt(plain_text, key):
    plain_numbers = text_to_numbers(plain_text)
    key_numbers = text_to_numbers(key)
    
    # Appliquer l'addition modulo 26
    cipher_numbers = [(p + k) % 26 for p, k in zip(plain_numbers, key_numbers)]
    
    cipher_text = numbers_to_text(cipher_numbers)
    return cipher_text

def otp_decrypt(cipher_text, key):
    cipher_numbers = text_to_numbers(cipher_text)
    key_numbers = text_to_numbers(key)
    
    # Appliquer la soustraction modulo 26
    plain_numbers = [(c - k) % 26 for c, k in zip(cipher_numbers, key_numbers)]
    
    plain_text = numbers_to_text(plain_numbers)
    return plain_text

plain_text = input("Entrez le texte clair : ").upper()
key = input("Entrez la clé secrète : ").upper()

if len(plain_text) != len(key):
    print("La longueur du texte clair et de la clé doivent être identiques.")
else:
    # Chiffrement
    cipher_text = otp_encrypt(plain_text, key)
    print(f"Message chiffré : {cipher_text}")

    # Déchiffrement
    decrypted_text = otp_decrypt(cipher_text, key)
    print(f"Message déchiffré : {decrypted_text}")
