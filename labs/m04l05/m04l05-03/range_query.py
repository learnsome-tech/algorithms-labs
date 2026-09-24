# Algorithms & Data Structures for Working Engineers — lesson m04l05 — Searching With Hashes Versus Trees
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l05
# © LearnSome.tech
import bisect

data = list(range(0, 1000, 3))
data_set = set(data)

def range_sorted(arr, lo, hi):
    l = bisect.bisect_left(arr, lo)
    r = bisect.bisect_right(arr, hi)
    return arr[l:r]

def range_set(s, lo, hi):
    return sorted(x for x in s if lo <= x <= hi)

print('sorted list range [100, 125]:', range_sorted(data, 100, 125))
print('set range [100, 125]:        ', range_set(data_set, 100, 125))
