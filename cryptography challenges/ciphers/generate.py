# test = ####REDACTED####
#What a wonderful welcome message to the CTF to test
#flag = ###REDACTED#####


import os
import base64
from itertools import cycle


key = ###REDACTED#####          key is of length 15

def xor(a,b) :
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

c1 = base64.b16encode(xor(test,key).encode())
c2 = base64.b16encode(xor(flag,key).encode())

print(c1,c2,key)
#Hint : Would it matter if my welcome message and flag share a word? Meh..who cares..I've used a strong key
