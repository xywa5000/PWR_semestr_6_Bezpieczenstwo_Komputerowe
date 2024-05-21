# zad_2.py

from rc4 import RC4, detect_same_key


def main():
    # Przykładowe dane
    key1 = "Key"
    key2 = "Other key"
    plaintext1 = "Hello World!"
    plaintext2 = "Goodbye World!"

    # Szyfrowanie za pomocą tego samego klucza
    ciphertext1 = RC4(key1, plaintext1)
    ciphertext2 = RC4(key1, plaintext2)

    # Wykrywanie użycia tego samego klucza
    same_key_used = detect_same_key(ciphertext1, ciphertext2)
    print(f"Same key used: {same_key_used}")

    # Szyfrowanie za pomocą innych kluczy
    ciphertext1 = RC4(key1, plaintext1)
    ciphertext2 = RC4(key2, plaintext2)

    # Wykrywanie użycia tego samego klucza
    same_key_used = detect_same_key(ciphertext1, ciphertext2)
    print(f"Same key used: {same_key_used}")

if __name__ == "__main__":
    main()