# Algorithms & Data Structures for Working Engineers — lesson m04l03 — Binary Search And Its Invariant
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l03
# © LearnSome.tech
def off_by_one(arr, t):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == t: return mid
        if arr[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
def fixed(arr, t):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == t: return mid
        if arr[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
data = list(range(0, 20, 2))
print('off-by-one on 18:', off_by_one(data, 18))
print('fixed on 18:', fixed(data, 18))
print('both on 8:', off_by_one(data, 8), fixed(data, 8))
