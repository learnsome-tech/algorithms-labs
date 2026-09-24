# Algorithms & Data Structures for Working Engineers — lesson m01l03 — Space, In-Place Work And The Call Stack
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l03
# © LearnSome.tech
import sys

original = list(range(5))
copy = original[::-1]
print('original:', original)
print('reversed:', copy)
print('original unchanged:', original)

sizes = [100, 1000, 10000]
for n in sizes:
    lst = list(range(n))
    print(n, sys.getsizeof(lst))
