def detect_ecb(ciphertexts):
    for ciphertext in ciphertexts:
        blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
        unique_blocks = set(blocks)
        if len(unique_blocks) != len(blocks):
            return ciphertext
    return None

# Read ciphertexts from file
with open("cryptopal8.txt", "r") as file:
    ciphertexts = [bytes.fromhex(line.strip()) for line in file]

# Detect ECB encryption
ecb_ciphertext = detect_ecb(ciphertexts)

if ecb_ciphertext:
    print("ECB encryption detected. Ciphertext:", ecb_ciphertext.hex())
else:
    print("ECB encryption not detected.")




#iterate through the ct,make them block of 16's,use set fn and make another set(this removes duplicates)
#if the length of original no of blocks and length of set block are unique,then there is ecb detected.
# note: identical plaintext blocks will always produce identical ciphertext blocks.
#Each block is encrypted separately
