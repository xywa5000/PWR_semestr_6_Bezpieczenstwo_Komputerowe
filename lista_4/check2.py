def extended_gcd(a, b):
    """
    Rozszerzony algorytm Euklidesa, który zwraca gcd(a, b) oraz współczynniki x i y takie, że ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    """
    Znajduje odwrotność multiplikatywną e modulo phi_n za pomocą rozszerzonego algorytmu Euklidesa.
    """
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("e nie ma odwrotności multiplikatywnej modulo phi(n)")
    else:
        return x % phi_n

def compute_d(e, phi_n):
    """
    Oblicza wartość d na podstawie równania d * e ≡ 1 (mod phi(n)).
    """
    return mod_inverse(e, phi_n)

# Przykład użycia:
e = 113
phi_n = 216  # przykładowa wartość φ(n)

d = compute_d(e, phi_n)
print(d)
