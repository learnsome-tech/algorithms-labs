EMPTY, TOMB = None, object()

def lp_put(table, k, v):
    n, i, probes = len(table), hash(k) % len(table), 0
    while True:
        probes += 1
        if table[i] is EMPTY or table[i] is TOMB:
            table[i] = (k, v); return probes
        if table[i][0] == k:
            table[i] = (k, v); return probes
        i = (i + 1) % n

table = [EMPTY] * 8
total = 0
for k in [3, 11, 19, 7, 15, 2]:
    total += lp_put(table, k, k * k)
print('total probes:', total)
filled = sum(1 for x in table if x not in (EMPTY, TOMB))
print('load:', filled, '/', len(table))
