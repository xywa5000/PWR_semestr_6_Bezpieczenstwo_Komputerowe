import random


def miller_rabin_test(n, k=20):
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
        """
        Sprawdza, czy n jest złożona dla danego świadka a.
        """
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
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        x2 = x1
        x1 = x
        
        d = y1
        y1 = x
    
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
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
    d = multiplicative_inverse(e, phi)
    return ((n, e), (n, d))

def modular_exponentiation(a, k, n):
    result = 1
    a = a % n
    while k > 0:
        if (k % 2) == 1:  # Jeśli k jest nieparzyste, pomnóż wynik przez a
            result = (result * a) % n
        k = k >> 1  # Podziel k przez 2
        a = (a * a) % n  # Podnieś a do kwadratu
    return result

def attack(n, e, d):
    # 1
    kphi = d * e - 1
    t = kphi

    # 2
    while (t%2==0):
        t=t//2
    
    # 3
    a = 2
    p=1
    while (a<100):
        # print(a)
        k = t
        flag = False
        while ( k<kphi):
            # x = (a ** k) % n
            x = modular_exponentiation(a, k, n)
            if (x!=t and x!=n-1 and (x*x)%n==1):
                p = gcd(x-1, n)
                flag = True
                break
            k = k * 2
        a = a + 2
        if flag:
            break
    q = n / p
    return p, q


if __name__ == '__main__':

    p = 13
    q = 19

    publicA, privateA = generate_keypair(p, q)
    publicB, privateB = generate_keypair(p, q)

    print("Generated keys:")
    print("PublicA: ", publicA)
    print("PrivateA: ", privateA)
    print("PublicB: ", publicB)
    print("PrivateB: ", privateB)

    print("\nattack with: public and private A:")
    print(publicA[0], publicA[1], privateA[1])
    p_prim, q_prim = attack(publicA[0], publicA[1], privateA[1])

    hacked_key = multiplicative_inverse(publicB[1], (p_prim-1)*(q_prim-1))
    print("original: ", privateB[1])
    print("hacked:   ", hacked_key)

    print("\nCheck:")
    print(f"de = {publicA[1]} * {privateA[1]} = {publicA[1] * privateA[1]}")
    de = publicA[1] * privateA[1]
    print(f"phi = ({p} - 1) * ({q} - 1) = {(p-1)*(q-1)}")
    phi = (p-1)*(q-1)
    print(de % phi)
