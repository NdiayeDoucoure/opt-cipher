import random

def text_to_numbers(text):
    return [(ord(char) - ord('A')) if char.isalpha() else char for char in text.upper()]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) if isinstance(num, int) else num for num in numbers)

def generate_random_key(length):
    return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(length))

def otp_encrypt(plain_text, key):
    plain_numbers = text_to_numbers(plain_text)
    key_numbers = text_to_numbers(key)

    cipher_numbers = [
        (p + k) % 26 if isinstance(p, int) else p
        for p, k in zip(plain_numbers, key_numbers)
    ]

    return numbers_to_text(cipher_numbers)

def otp_decrypt(cipher_text, key):
    cipher_numbers = text_to_numbers(cipher_text)
    key_numbers = text_to_numbers(key)

    plain_numbers = [
        (c - k) % 26 if isinstance(c, int) else c
        for c, k in zip(cipher_numbers, key_numbers)
    ]

    return numbers_to_text(plain_numbers)


plain_text = input("Entrez le texte clair : ")


key = generate_random_key(len(plain_text))
print(f"Clé aléatoire générée : {key}")


cipher_text = otp_encrypt(plain_text, key)
print(f"Message chiffré : {cipher_text}")


decrypted_text = otp_decrypt(cipher_text, key)
print(f"Message déchiffré : {decrypted_text}")