# zad_1.py

from rc4 import RC4, RC4_decrypt


def main():
    # Przykładowe dane
    key1 = "Key"
    key2 = "AnotherKey"
    plaintext = "Hello, World!"
    print(f"key1: {key1}\nkey2: {key2}\nmessage: {plaintext}")

    # Szyfrowanie za pomocą key1
    ciphertext1 = RC4(key1, plaintext)
    print(f"Ciphertext1 (key1): {ciphertext1}")

    # Szyfrowanie za pomocą key2
    ciphertext2 = RC4(key2, plaintext)
    print(f"Ciphertext2 (key2): {ciphertext2}")

    # Deszyfrowanie za pomocą key1
    decrypted_text1 = RC4_decrypt(key1, ciphertext1)
    print(f"Decrypted Text (key1): {decrypted_text1}")

    # Deszyfrowanie za pomocą key2
    decrypted_text2 = RC4_decrypt(key2, ciphertext2)
    print(f"Decrypted Text (key2): {decrypted_text2}")

if __name__ == "__main__":
    main()