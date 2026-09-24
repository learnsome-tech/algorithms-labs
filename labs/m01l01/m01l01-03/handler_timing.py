# Algorithms & Data Structures for Working Engineers — lesson m01l01 — Why Complexity Matters In Production
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m01l01
# © LearnSome.tech
import time

n = 10000
users_list = list(range(n))
users_dict = {i: True for i in range(n)}
target = n - 1
reps = 1000

t0 = time.perf_counter()
for _ in range(reps):
    found = target in users_list
list_time = time.perf_counter() - t0

t0 = time.perf_counter()
for _ in range(reps):
    found = target in users_dict
dict_time = time.perf_counter() - t0

print('dict lookup was faster:', dict_time < list_time)
print('ratio above five:', list_time / dict_time > 5)
