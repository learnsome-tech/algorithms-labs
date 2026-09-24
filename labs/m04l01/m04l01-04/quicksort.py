# Algorithms & Data Structures for Working Engineers — lesson m04l01 — Comparison Sorts: Insertion, Merge And Quicksort
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l01
# © LearnSome.tech
import random
def quicksort(arr):
    ct = [0]
    def sort(a, lo, hi):
        if lo >= hi: return
        pv = a[hi]; i = lo - 1
        for j in range(lo, hi):
            ct[0] += 1
            if a[j] <= pv: i += 1; a[i], a[j] = a[j], a[i]
        a[i+1], a[hi] = a[hi], a[i+1]
        sort(a, lo, i); sort(a, i+2, hi)
    work = arr[:]
    sort(work, 0, len(work) - 1)
    return work, ct[0]
random.seed(1)
data = [random.randint(0, 99) for _ in range(10)]
result, c = quicksort(data)
print('before:', data)
print('sorted:', result)
print('comparisons:', c)
print('verified:', result == sorted(data))
