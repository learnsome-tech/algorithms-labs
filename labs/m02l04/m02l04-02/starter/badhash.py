def bad_slot(k, n): return 0

def good_slot(k, n):
    h = 0
    for c in str(k):
        h = (h * 31 + ord(c)) % n
    return h

def insert_chain(keys, n, slot_fn):
    buckets = [[] for _ in range(n)]
    cmps = 0
    for k in keys:
        s = slot_fn(k, n)
        cmps += len(buckets[s])
        buckets[s].append(k)
    return cmps

n, keys = 16, list(range(12))
print('bad hash comparisons:', insert_chain(keys, n, bad_slot))
print('good hash comparisons:', insert_chain(keys, n, good_slot))
