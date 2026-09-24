# Algorithms & Data Structures for Working Engineers — lesson m07l01 — Divide And Conquer And The Recurrence
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m07l01
# © LearnSome.tech
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    steps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        steps += 1
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps

data = list(range(0, 128, 2))
idx, steps = binary_search(data, 64)
print('found 64 at index', idx, 'in', steps, 'steps')
_, miss = binary_search(data, 99)
print('search for 99 also took', miss, 'steps')
print('array has', len(data), 'elements')
