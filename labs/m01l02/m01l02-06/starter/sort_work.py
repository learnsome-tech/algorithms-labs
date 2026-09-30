import math

def count_merge_passes(n):
    passes = 0
    size = 1
    while size < n:
        size *= 2
        passes += 1
    return passes

sizes = [8, 64, 512, 4096]
for n in sizes:
    lg = count_merge_passes(n)
    work = n * lg
    print(n, lg, work)
