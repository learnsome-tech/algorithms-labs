# Algorithms & Data Structures for Working Engineers — lesson m03l05 — Choosing The Right Sequence
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l05
# © LearnSome.tech
import time
from collections import deque
n=20000
lst=list(range(n))
dq=deque(range(n))
t0=time.perf_counter()
for _ in range(n): lst.insert(0,0)
t_list=time.perf_counter()-t0
t0=time.perf_counter()
for _ in range(n): dq.appendleft(0)
t_deque=time.perf_counter()-t0
print('insert at front, deque faster:', t_deque<t_list)
lst2=list(range(n))
dq2=deque(range(n))
t0=time.perf_counter()
for _ in range(n): lst2[n//2]
t_idx=time.perf_counter()-t0
t0=time.perf_counter()
for _ in range(n): dq2[n//2]
t_didx=time.perf_counter()-t0
print('random access, list faster:', t_idx<t_didx)
