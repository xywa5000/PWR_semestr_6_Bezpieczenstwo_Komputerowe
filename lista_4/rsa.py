import random


def miller_rabin_test(n, k=40):
    """
    Przeprowadza test Millera-Rabina na liczbie n z k iteracjami.
    Zwraca True, jeśli n jest prawdopodobnie pierwsza, w przeciwnym razie False.
    
    n: liczba do sprawdzenia
    k: liczba iteracji testu
    """
    # Jeśli n jest mniejsze niż 2 lub jest parzysta (z wyjątkiem 2), to nie jest pierwsza
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Znajdź d i r takie, że n-1 = d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    def is_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
    
    # Przeprowadź k iteracji testu
    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_composite(a):
            return False
    
    return True


def is_prime(n):
    """
    Funkcja sprawdzająca czy podana liczba n jest pierwsza poprzez sprawdzenie potencjalnyuch dzielników do sqrt(n)
    """
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))


def gcd(a, b):
    """
    Klasyczny iteracyjny algorytm gcd
    """
    while b != 0:
        a, b = b, a % b
    return a


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


def generate_keypair(p, q):
    """
    Generuje parę kluczy (publiczny i prywatny) na podstawie dwóch (różnych!) liczb pierwszych
    """
    if not (miller_rabin_test(p) and miller_rabin_test(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((n, e), (n, d))


def modular_exponentiation(a, k, n):
    """
    Wylicza (a ** k) % n w spsoób, który minimalizuje ryzyko przepełnienia typu zmiennych
    """
    result = 1
    a = a % n
    while k > 0:
        if (k % 2) == 1:  # Jeśli k jest nieparzyste, pomnóż wynik przez a
            result = (result * a) % n
        k = k >> 1  # Podziel k przez 2
        a = (a * a) % n  # Podnieś a do kwadratu
    return result


def verify_keys(e, d, phi_n):
    """
    Sprawdza, czy d⋅e ≡ 1 (mod φ(n))
    """
    return (d * e) % phi_n == 1, (d * e) % phi_n


def attack(n, e, d):
    """
    Przeprowadza atak na klucz prywatny przy założeniu tego samego (p, q) dla atakującego i ofiary
    """
    # 1
    kphi = d * e - 1
    t = kphi

    # 2
    while (t % 2 == 0):
        t = t // 2
    
    # 3
    a = 2
    p = 1
    while (a<100):
        # print(a)
        k = t
        flag = False
        while (k < kphi):
            # x = (a ** k) % n
            x = modular_exponentiation(a, k, n)
            if (x != t and x != n - 1 and (x * x) % n == 1):
                p = gcd(x-1, n)
                flag = True
                break
            k = k * 2
        a = a + 2
        if flag:
            break
    q = n // p
    return p, q
