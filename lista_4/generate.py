from rsa import generate_keypair, gcd, verify_keys

if __name__ == '__main__':

    # p = 13
    # q = 19

    # p = 2575723
    # q = 6108889

    p = 1093642035933744490193948789329
    q = 5218288973937920616127738686311

    public, private = generate_keypair(p, q)

    print("\nGenerated keys:")
    print("PublicA:  ", public)
    print("PrivateA: ", private)

    print("\nCheck")
    n = p * q
    print(f"n = p * q = {p} * {q} = {n}")
    phi = (p - 1) * (q - 1)
    print(f"phi = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi}")
    print(f"1 = gcd(e, phi) = gcd({public[1]}, {phi}) = {gcd(public[1], phi)}")
    print(f"d * e = 1 mod phi => ({public[1]} * {private[1]}) mod {phi} = {(public[1] * private[1]) % phi}\n")

    print(f"Verify keys: {verify_keys(public[1], private[1], phi)}\n")
