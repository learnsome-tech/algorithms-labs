def weak_slot(key, n):
    return sum(ord(c) for c in key) % n

def poly_slot(key, n, base=31):
    h = 0
    for ch in key:
        h = (h * base + ord(ch)) % n
    return h

words = ['star', 'arts', 'tars', 'rats', 'tsar']
n = 16
weak = [weak_slot(w, n) for w in words]
poly = [poly_slot(w, n) for w in words]
print('words:', words)
print('weak slots (sum of codes):', weak)
print('distinct weak slots:', len(set(weak)))
print('poly slots (base-31):', poly)
print('distinct poly slots:', len(set(poly)))
