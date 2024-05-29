from rsa import generate_keypair, attack, mod_inverse

if __name__ == '__main__':

    # p = 13
    # q = 19

    # p = 2575723
    # q = 6108889

    p = 1093642035933744490193948789329
    q = 5218288973937920616127738686311

    publicA, privateA = generate_keypair(p, q)
    publicB, privateB = generate_keypair(p, q)

    print("\nGenerated keys:")
    print("PublicA:  ", publicA)
    print("PrivateA: ", privateA)
    print("PublicB:  ", publicB)
    print("PrivateB: ", privateB)

    print("\nAttack:")
    print("Known values: PublicA, PrivateA and PublicB")
    print("Attacked value: PrivateB")

    p_prim, q_prim = attack(publicA[0], publicA[1], privateA[1])
    print(f"p, q: {p_prim:d}, {str(q_prim)}")
    hacked_key = mod_inverse(publicB[1], (p_prim-1)*(q_prim-1))

    if hacked_key is not None:
        print(f"original PrivateB: {privateB[1]}")
        print(f"hacked PrivateB:   {int(hacked_key)}")
        if privateB[1] == int(hacked_key):
            print("Success!\n")
        else:
            print("Failure!\n")
    else:
        print("Attack failed\n")
