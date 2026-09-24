# Algorithms & Data Structures for Working Engineers — lesson m04l03 — Binary Search And Its Invariant
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l03
# © LearnSome.tech
def first_true(pred, lo, hi):
    # Invariant: pred is False below lo, True at or above hi
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# integer square root: smallest k with k*k >= n
n = 144
k = first_true(lambda x: x * x >= n, 0, n)
print(f'integer sqrt of {n} is {k}')

# minimum pages to hold n records at cap per page
records = 10000
cap = 250
pages = first_true(lambda p: p * cap >= records, 0, records)
print(f'minimum pages: {pages}')
