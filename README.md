# Compress-Lattice-Crypto

This program is a proof-of-concept implementation of key, signature, and ciphertext size reductino for lattice-based cryptography, written in SageMath 9.0.

# Load the code 

'''
load('LatticeCompression.py')
'''

# Parameter Settings, public key

## Kyber512

'''
q = 3329
n = 256
k = 2
'''

## Falcon-512, public key

'''
q = 12289
n = 512
k = 1
'''

## CRYSTALS-Dilithium NIST security level 1, (part of) signature

'''
q = 2^17 + 90
n = 256
k = 3
'''


# Generate a sample key

A random element in R_q^k is generated. 

'''
t = get_key(n, k, q)
print_key(t, n, k, q)
'''

# Compress key

'''
num = compress_key(t, n, k, q)
'''

# Decompress key

'''
decomp = decompress_key(num, n, k, q)
'''

# Test the compression/decompression

'''
compare_keys(t, decomp, n, k,q)
'''

