import hashlib

def slot(k, n):
    return int(hashlib.sha256(str(k).encode()).hexdigest(), 16) % n

def load(b): return sum(len(x) for x in b) / len(b)

def needs_resize(b): return load(b) > 0.7

buckets = [[] for _ in range(4)]
words = ['red', 'green', 'blue', 'gold', 'pink']
for w in words:
    s = slot(w, len(buckets))
    buckets[s].append(w)
    lf = round(load(buckets), 2)
    resize = needs_resize(buckets)
    print(w, '->', s, '| load', lf, '| resize?', resize)
