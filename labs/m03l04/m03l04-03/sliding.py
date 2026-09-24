# Algorithms & Data Structures for Working Engineers — lesson m03l04 — Deques And Ring Buffers
# https://learnsome.tech/courses/algorithms-course/watch?lesson=m03l04
# © LearnSome.tech
from collections import deque
def sliding_max(data, k):
    window=deque(maxlen=k)
    results=[]
    for x in data:
        window.append(x)
        if len(window)==k:
            results.append(max(window))
    return results
data=[3,1,4,1,5,9,2,6,5,3]
k=3
print('data:', data)
print('max per window:', sliding_max(data,k))
