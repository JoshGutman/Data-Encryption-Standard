#!/usr/bin/env python

import random

"""
DES Key Scheduler:

    - Generates 16 48-bit subkeys from a randomly
      generated 64-bit initial key

    - Returns a list of the 16 subkeys in the form
      of binary strings

"""

def key_scheduler():

    # -------------------- Variables -------------------- #
    #
    # k         Initial 64-bit key
    # k_prime   Permuted 56-bit key
    # c0        Left half of k_prime
    # d0        Right half of k_prime
    # c_keys    16 28-bit permutations of c0 using lrt
    # d_keys    16 28-bit permutations of d0 using lrt
    # keys      Final list of 16 48-bit keys
    #
    # --------------------------------------------------- #

    
    # ---------------- Hard-Coded Values ---------------- #

    # pc1       Permutation table No. 1
    pc1 = [57, 49, 41, 33, 25, 17,  9,
            1, 58, 50, 42, 34, 26, 18,
           10,  2, 59, 51, 43, 35, 27,
           19, 11,  3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
           14,  6, 61, 53, 45, 37, 29,
           21, 13,  5, 28, 20, 12,  4]

    # pc2       Permutation table No. 2
    pc2 = [14, 17, 11, 24,  1,  5,
           3,  28, 15,  6, 21, 10,
           23, 19, 12,  4, 26,  8,
           16,  7, 27, 20, 13,  2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]
           

    # lrt       Left rotation table
    lrt = [1, 1, 2, 2, 2, 2, 2, 2,
           1, 2, 2, 2, 2, 2, 2, 1]

    # --------------------------------------------------- #


    

    # Generate random 64-bit number
    # Note - Even though the algorithm starts with a 64-bit key, DES is still technically
    # 56-bit, because 8 of the bits are used as parity bits. These bits are lost during the
    # first permutation using pc1.
    k = random.getrandbits(64)
    k = bin(k)[2:].zfill(64)
    

    # Generate k_prime using permutation table 1
    k_prime = ""
    for number in pc1:
        k_prime += k[number-1]
        

    # Find c0 (left half of k_prime) and d0 (right half of k_prime)
    c0 = k_prime[:28]
    d0 = k_prime[28:]


    # Rotate c0 and d0 according to left rotation table
    c_keys = []
    d_keys = []
    for i in range(16):
        num = lrt[i]
        
        temp = c0[0:num]
        c0 = c0[num:] + temp
        c_keys.append(c0)

        temp = d0[0:num]
        d0 = d0[num:] + temp
        d_keys.append(d0)


    # Generate subkeys by combining c_keys[i] and d_keys[i].
    # Use permutation table 2 to generate 16 48-bit keys
    keys = []
    for i in range(16):
        cat = c_keys[i] + d_keys[i]
        temp = ""
        for number in pc2:
            temp += cat[number-1]
        keys.append(temp)


    return keys


