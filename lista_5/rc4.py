# rc4.py

def KSA(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key, data):
    """RC4 encryption/decryption"""
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S)
    result = []
    for char in data:
        val = ("%02X" % (ord(char) ^ next(keystream)))
        result.append(val)
    return ''.join(result)

def RC4_decrypt(key, data):
    """RC4 decryption"""
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S)
    result = []
    for i in range(0, len(data), 2):
        byte = int(data[i:i+2], 16)
        val = chr(byte ^ next(keystream))
        result.append(val)
    return ''.join(result)

def hex_to_bytes(hex_str):
    """Convert hex string to bytes"""
    return bytes.fromhex(hex_str)

def detect_same_key(ciphertext1, ciphertext2):
    """Detect if the same key was used for two ciphertexts"""
    b_ciphertext1 = hex_to_bytes(ciphertext1)
    b_ciphertext2 = hex_to_bytes(ciphertext2)
    for i in range(min(len(b_ciphertext1), len(b_ciphertext2))):
        if (b_ciphertext1[i] ^ b_ciphertext2[i]) >= 0x80:
            return False
    return True
