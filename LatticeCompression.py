def get_key(n, k, q):
    module = []
    for i in range(k):
        poly = []
        for j in range(n):
            poly.append(randrange(q))
        module.append(poly)    
    return module

def print_key(t, n, k, q):
    
    for i in range(k):
        line = "Poly %d: "%i 
        line += "%d"%(t[i][0])
        for j in range(1, n):
            line += " + %d*x^%d"%(t[i][j], j)
        print(line)

def comperess_key(t, n, k, q):
    num = 0
    qpow = 1
    for i in range(k):
        for j in range(n):
            num += t[i][j] * qpow
            qpow *= q
    
    return num

def decompress_key(num, n, k, q):
    temp = num.digits(q)
    temp += [0] * (n*k - len(temp))
    decomp = [temp[i*n: (i+1)*n] for i in range(k)]

    return decomp



def compare_keys(key1, key2, n, k, q):
    for i in range(k):
        for j in range(n):
            if key1[i][j] != key2[i][j]:
                return False
            
    return True



q = 2^19 + 120
n = 256  
k = 9
