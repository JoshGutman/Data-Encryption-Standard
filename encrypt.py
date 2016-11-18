#!/usr/bin/env python

from f_function import f

def encrypt(text, keys):

    # Split text up into 64-bit chunks
    blocks = []
    for i in range(0, len(text), 8):
        blocks.append(text[i:i+8])


    # Encrypt chunks
    e_list = []
    for block in blocks:
        e_list.append(_cipher(_ascii_to_bin(block), keys))


    # Combine chunks back into a single string
    out = ""
    for block in e_list:
        #out += _bin_to_ascii(block)    # ASCII output
        #out += hex(int(block, 2))      # Hex output
        out += block                    # Binary output


    return out



def _cipher(bit64, keys):

    # Initial permutation table
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17,  9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    # Final permutation
    fp = [40,  8, 48, 16, 56, 24, 64, 32,
          39,  7, 47, 15, 55, 23, 63, 31,
          38,  6, 46, 14, 54, 22, 62, 30,
          37,  5, 45, 13, 53, 21, 61, 29,
          36,  4, 44, 12, 52, 20, 60, 28,
          35,  3, 43, 11, 51, 19, 59, 27,
          34,  2, 42, 10, 50, 18, 58, 26,
          33,  1, 41,  9, 49, 17, 57, 25]
    

    # Perform initial permutation on block
    p = ""
    for number in ip:
        p += bit64[number-1]


    # Split block into two halves
    ln = p[:32]
    rn = p[32:]

    # 16 rounds of encryption, rotating and XORing each half after each round
    for i in range(16):
        temp = rn
        rn = bin(int(ln, 2) ^ int(f(rn, keys[i]), 2))[2:].zfill(32)
        ln = temp


    # Combine left and right halves and perform final permutation
    combined = ln + rn
    out = ""
    for number in fp:
        out += combined[number-1]


    return out






# Convert ASCII text to binary
def _ascii_to_bin(text):

    out = ""
    for letter in text:
        out += bin(ord(letter))[2:].zfill(8)

    # Pad block with 0s if necessary
    for i in range(64-(len(out))):
        out += "0"

    return out



# Convert binary to ASCII text
def _bin_to_ascii(bit64):

    out = ""
    for i in range(0, 64, 8):
        out += chr(int(bit64[i:i+8], 2))

    #out.replace("\x00", "")
    return out
