# Algorithms & Data Structures for Working Engineers — lesson m04l02 — Counting And Radix Sort: Beating N Log N
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l02
# © LearnSome.tech
def radix_sort(arr, digits=3):
    base = 10
    result = arr[:]
    for d in range(digits):
        buckets = [[] for _ in range(base)]
        for v in result:
            buckets[(v // (base ** d)) % base].append(v)
        result = []
        for bucket in buckets:
            result.extend(bucket)
    return result

import random
random.seed(1)
data = [random.randint(0, 999) for _ in range(10)]
print('input: ', data)
result = radix_sort(data)
print('sorted:', result)
print('verified:', result == sorted(data))
