def verify_keys(e, d, phi_n):
    """
    Sprawdza, czy d⋅e ≡ 1 (mod φ(n)).
    
    :param e: public exponent
    :param d: private exponent
    :param phi_n: Euler's totient function value for n
    :return: True if the equality holds, otherwise False
    """
    return (d * e) % phi_n == 1, (d * e) % phi_n

# Przykład użycia:
e = 65
d = 113
phi_n = 216  # przykładowa wartość φ(n)

is_valid = verify_keys(e, d, phi_n)
print(is_valid)  # Powinno wydrukować True, jeśli równość jest zachowana
