from encrypt import encrypt
from decrypt import decrypt


# Triple encryption with 3 separate key sets.
# C = E(D(E(P, k3), k2), k1)
def tcc_encrypt(text, key1, key2, key3):

    return encrypt(decrypt(encrypt(text, key3), key2), key1)


# Triple decryption with 3 separate key sets.
# P = D(E(D(C, k1), k2), k3)
def tcc_decrypt(cipher, key1, key2, key3):

    return decrypt(encrypt(decrypt(cipher, key1), key2), key3)

