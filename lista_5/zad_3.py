# zad_3.py

import random
from itertools import combinations
from rc4 import RC4, hex_to_bytes

def gen_bank_numbers(q):
    bank_numbers = []
    numery_rozliczeniowe = [
        [1, 0, 1, 0, 0, 0, 0, 0], # NBP
        [1, 1, 6, 0, 0, 0, 0, 6], # Millenium
        [1, 0, 5, 0, 0, 0, 0, 2], # ING
        [2, 1, 2, 0, 0, 0, 0, 1], # Santander
        [1, 0, 2, 0, 0, 0, 0, 3], # PKO BP
    ]
    rng = random.Random(2137)
    for nr in numery_rozliczeniowe:
        for _ in range(q):
            bank_number = ""
            client_number = [rng.randint(0, 9) for _ in range(16)]
            tmp = 212500
            for i in range(8):
                tmp += nr[i] * 10 ** (7 - i + 21)
            for i in range(16):
                tmp += client_number[i] * 10 ** (15 - i + 5)
            tmp = tmp % 97
            tmp = 98 - tmp
            bank_number += f"{tmp:02}"
            bank_number += ''.join(map(str, nr))
            bank_number += ''.join(map(str, client_number))
            bank_numbers.append(bank_number)
    return bank_numbers

def main():
    bank_numbers = gen_bank_numbers(2)
    key = "Very Good Key"
    cryptograms = []
    for bank_number in bank_numbers:
        cryptogram = RC4(key, bank_number)
        cryptograms.append(cryptogram)
    
    for c0, c1 in combinations(cryptograms, 2):
        b_c0 = hex_to_bytes(c0)
        b_c1 = hex_to_bytes(c1)
        xored = [i0 ^ i1 for i0, i1 in zip(b_c0, b_c1)]
        #print(xored[2:10])
        print(xored)

if __name__ == "__main__":
    main()
