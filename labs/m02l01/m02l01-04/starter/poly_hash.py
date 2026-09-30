def poly_hash(key, n, base=31):
    h = 0
    for ch in key:
        h = (h * base + ord(ch)) % n
    return h

words = ['ant', 'bee', 'cat', 'dog', 'elk',
         'fox', 'gnu', 'hen']
counts = [0] * 8
for w in words:
    counts[poly_hash(w, 8)] += 1
for i, c in enumerate(counts):
    print(f'bucket {i}: {c}')
