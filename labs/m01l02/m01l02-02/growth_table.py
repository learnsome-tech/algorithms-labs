# Algorithms & Data Structures for Working Engineers — lesson m01l02 — Recognising The Common Growth Rates
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l02
# © LearnSome.tech
import math

sizes = [10, 100, 1000, 10000]
print('n        const  logn  linear  nlogn      quad')
for n in sizes:
    lg = int(math.log2(n))
    print(n, 1, lg, n, n * lg, n * n)
