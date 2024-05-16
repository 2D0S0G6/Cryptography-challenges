c1 = '2E0A193C0802117F0007451C3F23'
c2 = '1F0314381C37440D2B5B0B3C191C090D5E4531385E4100321D0B22'
def xor(a,b) :
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

