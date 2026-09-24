# Algorithms & Data Structures for Working Engineers — lesson m04l02 — Counting And Radix Sort: Beating N Log N
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m04l02
# © LearnSome.tech
def counting_sort(arr, k):
    counts = [0] * k
    for v in arr: counts[v] += 1
    result = []
    for v, c in enumerate(counts): result.extend([v] * c)
    return result

small = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print('small range:', counting_sort(small, 10))

for k in [10, 100, 100000]:
    overhead = k * 8
    print(f'k={k}: count array needs {overhead} bytes')
