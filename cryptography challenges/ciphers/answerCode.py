import os
import base64
from itertools import cycle

def xor(a, b):
    return [i ^ j for i, j in zip(a, cycle(b))]

def crib_drag(c, crib):    
    results = []
    for index in range(len(c) - len(crib) + 1):
        single_result = b''
        for a, b in zip(c[index:index+len(crib)], crib):
            single_result += bytes([a ^ b])
        results.append(single_result.decode())
    return results


c1 = bytearray.fromhex('2E0A193C0802117F0007451C3F23')
c2 = bytearray.fromhex('1F0314381C37440D2B5B0B3C191C090D5E4531385E4100321D0B22')

print(xor(c1, c2))

#What a wonderful welcome message to the CTF to test

test_crib = b"welcome to CTF"
potential_plaintext = crib_drag(c1, test_crib)
print("Potential plaintext:", potential_plaintext)




# xor(a, b):

# This function performs an XOR operation between two byte arrays a and b.
# It uses the zip function to iterate over corresponding elements of the two arrays and the cycle function from itertools to cycle through the elements of b when its length is shorter than a.
# The XOR result for each pair of elements is stored in a list, which is returned.


# crib_drag(c, crib):

# This function performs a crib dragging attack on a ciphertext c given a crib (part of the plaintext).
# It iterates through each possible position in the ciphertext where the crib could match.
# For each position, it XORs the corresponding substring of the ciphertext with the crib and appends the resulting potential plaintext to a list.
# The list of potential plaintexts is returned.

# It XORs c1 and c2 and prints the result.
# It attempts a crib dragging attack using the crib "welcome to CTF" on c1, providing potential plaintexts based on the XOR operation with the crib.