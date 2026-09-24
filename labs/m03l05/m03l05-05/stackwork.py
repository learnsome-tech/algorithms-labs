# Algorithms & Data Structures for Working Engineers — lesson m03l05 — Choosing The Right Sequence
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l05
# © LearnSome.tech
from collections import deque
import time
n=30000
lst=list(range(n))
dq=deque(range(n))
t0=time.perf_counter()
for i in range(n): lst.append(i); lst.pop()
t_lst=time.perf_counter()-t0
t0=time.perf_counter()
for i in range(n): dq.append(i); dq.pop()
t_dq=time.perf_counter()-t0
print('stack on list vs deque near equal:', 0.2<t_lst/t_dq<5.0)
