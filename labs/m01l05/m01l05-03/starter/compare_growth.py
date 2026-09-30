def copies_fixed(n, step=4):
    cap, length, total = step, 0, 0
    for _ in range(n):
        if length == cap:
            total += length
            cap += step
        length += 1
    return total

def copies_doubling(n):
    cap, length, total = 1, 0, 0
    for _ in range(n):
        if length == cap:
            total += length
            cap *= 2
        length += 1
    return total

for n in [16, 64, 256]:
    print(n, copies_fixed(n), copies_doubling(n))
